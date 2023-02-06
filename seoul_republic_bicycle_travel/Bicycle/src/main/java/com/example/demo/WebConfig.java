package com.example.demo;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class WebConfig implements WebMvcConfigurer {
    @Override
    public void addResourceHandlers(ResourceHandlerRegistry registry) {
        registry.addResourceHandler("/Users/Pictures/**")
                .addResourceLocations("file:///Users/Pictures/");
    }
    // "classpath:/Users/Pictures/"
    // "file://C:/Users/Pictures/"
}
