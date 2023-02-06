package com.example.demo.user;

import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotEmpty;
import jakarta.validation.constraints.Size;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class UserCreateForm {

    @NotEmpty(message = "The name is required.")
    private String nickname;

    @Size(min = 3, max = 25)
    @NotEmpty(message = "User ID is required.")
    private String username;

    @NotEmpty(message = "Password is required.")
    private String password1;

    @NotEmpty(message = "Password verification is required.")
    private String password2;

    @NotEmpty(message = "Email is required.")
    @Email
    private String email;

    private Boolean agreeTerms;

}
