package com.example.demo.public_bike_rental_office_yeongdeungpo_gu;

import java.security.Principal;
import java.time.LocalDateTime;
import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.example.demo.mycourse.course;
import com.example.demo.mycourse.courseRepository;
import com.example.demo.user.SiteUser;
import com.example.demo.user.UserService;

import jakarta.persistence.Id;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.validation.Valid;
// import org.springframework.web.bind.annotation.RequestMethod;
// import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
@Controller
// @CrossOrigin(origins = "https://naveropenapi.apigw.ntruss.com") 
@RequestMapping("/rental")
public class rentalController {
    private static final SiteUser SiteUser = null;
    private final UserService userService;
    private final rentalService rentalService;
    private final seoulService seoulService;
    private final courseRepository courseRepository;

    
    
    @GetMapping("/rental_office")
    public String rental_office(Model model, @RequestParam(value = "keyword", defaultValue = "국회의원회관")String keyword) {
        model.addAttribute("offices", rentalService.getAllrental());
        model.addAttribute("place", rentalService.getplace(keyword));
        return "rental_office";
    }
    @GetMapping("/mycourse")
    public String mycourse(Model model, Principal principal) {
        model.addAttribute("offices", rentalService.getAllrental());
        model.addAttribute("places", seoulService.getAllplaces());
        model.addAttribute("test", "hello");
        SiteUser siteUser = this.userService.getUser(principal.getName());
        model.addAttribute("course", courseRepository.findByAuthor(siteUser));
        return "mycourse";
    }
    @GetMapping("/detail/{id}")
    public String detail(Model model,@PathVariable("id") Integer id,Principal principal) {
        SiteUser siteUser = this.userService.getUser(principal.getName());
        model.addAttribute("detail", courseRepository.findByIdAndAuthor(id,siteUser));
        return "course_detail";
    }
    @GetMapping("/delete/{id}")
    public String delete(Model model,@PathVariable("id") Integer id,Principal principal) {
        SiteUser siteUser = this.userService.getUser(principal.getName());
        courseRepository.deleteByIdAndAuthor(id,siteUser);
        return "redirect:/rental/mycourse";
    }

    @GetMapping("/save")
    public String save(@RequestParam(value="name1") String name1,
                        @RequestParam(value="lat1") String lat1,
                        @RequestParam(value="lng1") String lng1,
                        @RequestParam(value="name2") String name2,
                        @RequestParam(value="lat2") String lat2,
                        @RequestParam(value="lng2") String lng2,
                        @RequestParam(value="name3") String name3,
                        @RequestParam(value="lat3") String lat3,
                        @RequestParam(value="lng3") String lng3,
                        @RequestParam(value="name4") String name4,
                        @RequestParam(value="lat4") String lat4,
                        @RequestParam(value="lng4") String lng4,
                        @RequestParam(value="name5") String name5,
                        @RequestParam(value="lat5") String lat5,
                        @RequestParam(value="lng5") String lng5,
                        Principal principal,
                        Model model){
        // for(String place : result){
        //     System.out.println(place);
        //     System.out.println(make);
        //     // SiteUser siteUser = this.userService.getUserID(principal.getID());
        //     Course entity = Course.builder().place(place).make(make).build();
        //     courseRepository.save(entity);
        // }
        SiteUser siteUser = this.userService.getUser(principal.getName());
        course entity = course.builder().name1(name1).lat1(lat1).lng1(lng1).name2(name2).lat2(lat2).lng2(lng2).name3(name3).lat3(lat3).lng3(lng3).name4(name4).lat4(lat4).lng4(lng4).name5(name5).lat5(lat5).lng5(lng5).author(siteUser).build();
        courseRepository.save(entity);
        
        // model.addAttribute("course", courseRepository.findByAuthor(siteUser));
        // System.out.println("내 코스는 : "+courseRepository.findByAuthor(siteUser));
        return "redirect:/rental/mycourse";
    }
    

    
}
