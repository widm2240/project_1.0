package com.example.demo.user;

import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.stereotype.Controller;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
@Controller
@RequestMapping("/user")
public class UserController {

    private final UserService userService;
    
    @GetMapping("/signup")
    public String signup(UserCreateForm userCreateForm) {
        return "signup_form";
    }
    @PostMapping("/signup")
    public String signup(@Valid UserCreateForm userCreateForm, BindingResult bindingResult) {
        if (bindingResult.hasErrors()){
            return "signup_form";
        }

        if (!userCreateForm.getPassword1().equals(userCreateForm.getPassword2())) {
            bindingResult.rejectValue("password2", "passwordInCorrect",
            "The two passwords do not match.");
            return "signup_form";
        }
        if (userCreateForm.getAgreeTerms().equals(false)) {
            bindingResult.rejectValue("agreeTerms", "notAgreeTerms",
            "You have not agreed to the Terms and Conditions.");
            return "signup_form";
        }
        
        try {
            userService.create(userCreateForm.getNickname(),
            userCreateForm.getUsername(), 
            userCreateForm.getEmail(), 
            userCreateForm.getPassword1());
        } catch (DataIntegrityViolationException e) {
            e.printStackTrace();
            bindingResult.reject("singupFailed"," Already a registered user.");
            return "signup_form";
        } catch (Exception e) {
            e.printStackTrace();
            bindingResult.reject("singupFailed", e.getMessage());
            return "signup_form";
        }
        
        return "redirect:/";
    }

    @GetMapping("/login")
    public String login() {
        return "login_form";
    }


    @GetMapping("/course")
    public String course(){
        return "course";
    }

    @GetMapping("/Yeouido")
    public String Yeouido(){
        return "Yeouido";
    }

    @GetMapping("/Bukchon_Hanok_Village")
    public String Bukchon_Hanok_Village(){
        return "Bukchon_Hanok_Village";
    }
    @GetMapping("/Cheonggyecheon_Stream")
    public String Cheonggyecheon_Stream(){
        return "Cheonggyecheon_Stream";
    }
    
}
