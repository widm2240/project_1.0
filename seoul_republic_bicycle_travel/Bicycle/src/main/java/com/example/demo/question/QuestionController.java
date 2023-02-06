package com.example.demo.question;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.Principal;
import java.time.LocalDate;
import java.util.UUID;
import org.springframework.data.domain.Page;
import org.springframework.http.HttpStatus;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.springframework.web.server.ResponseStatusException;
import org.springframework.web.servlet.ModelAndView;

import com.example.demo.answer.AnswerForm;
import com.example.demo.user.SiteUser;
import com.example.demo.user.UserService;

import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;


@RequestMapping("/question")
@RequiredArgsConstructor
@Controller
public class QuestionController {

    private final QuestionService questionService;
    private final UserService userService;

    @RequestMapping("/list")
    public String list(Model model, 
        @RequestParam(value = "page", defaultValue = "0") int page,
        @RequestParam(value = "kw", defaultValue = "") String kw) {
        Page<Question> paging = this.questionService.getList(page, kw);
        Page<Question> paging2 = this.questionService.outDated(page, kw);
        Page<Question> paging3 = this.questionService.Views(page, kw);
        model.addAttribute("paging",paging);
        model.addAttribute("paging2", paging2);
        model.addAttribute("paging3", paging3);
        model.addAttribute("kw", kw);
        return "question_list";
    }

    @GetMapping(value = "/detail/{id}")
    public String detail(Model model, @PathVariable("id") Integer id, AnswerForm answerForm,
    HttpServletRequest request,
    HttpServletResponse response) {
        
        Cookie oldCookie = null;
		Cookie[] cookies = request.getCookies();
        
		if (cookies != null) {
			for (Cookie cookie : cookies) {
				if (cookie.getName().equals("postView")) {
					oldCookie = cookie;
				}
			}
		}
		
		if (oldCookie != null) {
			if (!oldCookie.getValue().contains("["+ id.toString() +"]")) {
				this.questionService.updateView(id);
				oldCookie.setValue(oldCookie.getValue() + "_[" + id + "]");
				oldCookie.setPath("/");
				oldCookie.setMaxAge(60 * 60 * 24); 							// 쿠키 시간
				response.addCookie(oldCookie);
			}
		} else {
			this.questionService.updateView(id);
			Cookie newCookie = new Cookie("postView", "[" + id + "]");
			newCookie.setPath("/");
			newCookie.setMaxAge(60 * 60 * 24); 								// 쿠키 시간
			response.addCookie(newCookie);
		}
        
        Question question = this.questionService.getQuestion(id);
        model.addAttribute("question", question);
        return "question_detail";
    }

    @PreAuthorize("isAuthenticated()")
    @GetMapping("/create")
    public String questionCreate(QuestionForm questionForm, Model model, Principal principal) {  
        return "question_form";
    }

    @PreAuthorize("isAuthenticated()")
    @PostMapping("/create")
    public String questionCreate(@Valid QuestionForm questionForm, 
        BindingResult bindingResult, Principal principal) throws Exception {
        if (bindingResult.hasErrors()){
            return "question_form";
        }
        SiteUser siteUser = this.userService.getUser(principal.getName());
        this.questionService.create(questionForm.getSubject(), 
            questionForm.getContent(), siteUser);// 질문을 저장한다.
        return "redirect:/question/list"; // 질문 저장후 질문 목록으로 이동한다.
    }

    @PreAuthorize("isAuthenticated()")
    @GetMapping("/modify/{id}")
    public String questionModify(QuestionForm questionForm, @PathVariable("id") Integer id, Principal principal) {
        Question question = this.questionService.getQuestion(id);
        if (principal.getName().equals("admin")){
            questionForm.setSubject(question.getSubject());
            questionForm.setContent(question.getContent());
            return "question_form";
        }
        else if(!question.getAuthor().getUsername().equals(principal.getName())) {
            throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "수정권한이 없습니다.");
        }
        questionForm.setSubject(question.getSubject());
        questionForm.setContent(question.getContent());
        return "question_form";
    }

    @PreAuthorize("isAuthenticated()")
    @PostMapping("/modify/{id}")
    public String questionModify(@Valid QuestionForm questionForm, BindingResult bindingResult,
        Principal principal, @PathVariable("id") Integer id) throws Exception {
            if (bindingResult.hasErrors()) {
                return "question_form";
            }
            Question question = this.questionService.getQuestion(id);
            if (principal.getName().equals("admin")){
                this.questionService.modify(question, questionForm.getSubject(), questionForm.getContent());
                return String.format("redirect:/question/detail/%s", id);
            }
            else if (!question.getAuthor().getUsername().equals(principal.getName())) {
                throw new ResponseStatusException(HttpStatus.BAD_REQUEST,"수정권한이 없습니다.");
            }
            this.questionService.modify(question, questionForm.getSubject(), questionForm.getContent());
            return String.format("redirect:/question/detail/%s", id);
        }
    
    @PreAuthorize("isAuthenticated()")
    @GetMapping("/delete/{id}")
    public String questionDelete(Principal principal, @PathVariable("id") Integer id) {
        Question question = this.questionService.getQuestion(id);
        if (principal.getName().equals("admin")){
            this.questionService.delete(question);
            return "redirect:/question/list";
        }
        else if (!question.getAuthor().getUsername().equals(principal.getName())){
            throw new ResponseStatusException(HttpStatus.BAD_REQUEST,"삭제 권한이 없습니다.");
        }
        this.questionService.delete(question);
        return "redirect:/question/list";
    }

    @PreAuthorize("isAuthenticated()")
    @GetMapping("/vote/{id}")
    public String questionVote(Principal principal, @PathVariable("id") Integer id) {
        Question question = this.questionService.getQuestion(id);
        SiteUser siteUser = this.userService.getUser(principal.getName());
        this.questionService.vote(question, siteUser);
        return String.format("redirect:/question/detail/%s", id);
    }

   
    
    @PreAuthorize("isAuthenticated()")
    @PostMapping("/create/upload")
    public ModelAndView imageUpload(MultipartHttpServletRequest request) throws Exception {
        LocalDate now = LocalDate.now();
        ModelAndView mav = new ModelAndView("jsonView");
        MultipartFile uploadFile = request.getFile("upload");
        // String originalFileName = uploadFile.getOriginalFilename();
        // String ext = originalFileName.substring(originalFileName.indexOf("."));
        String ext = ".png";
		String newFileName = UUID.randomUUID() + ext;
		String realPath = "C:/Users/Pictures/";
        String savePath = realPath + now + "/" + newFileName;
        String uploadPath = "/Users/Pictures/" + now + "/" + newFileName;
		File file = new File(savePath);
        if (!file.exists()) {
            try{
                Files.createDirectories(Paths.get(savePath));
                } 
                catch(Exception e){
                e.getStackTrace();
            }        
        }
		uploadFile.transferTo(file);
        mav.addObject("uploaded", true);
        mav.addObject("url", uploadPath);
        return mav;
    }

}
