package com.example.demo.mycourse;

import com.example.demo.user.SiteUser;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.ManyToOne;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
@AllArgsConstructor
@NoArgsConstructor
@Builder
@Entity
@Getter
@Setter
public class course {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;
    private String name1;
    private String lat1;
    private String lng1;
    private String name2;
    private String lat2;
    private String lng2;
    private String name3;
    private String lat3;
    private String lng3;
    private String name4;
    private String lat4;
    private String lng4;
    private String name5;
    private String lat5;
    private String lng5;

    @ManyToOne
    private SiteUser author;
}
