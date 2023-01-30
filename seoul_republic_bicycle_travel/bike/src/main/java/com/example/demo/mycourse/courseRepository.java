package com.example.demo.mycourse;

import java.util.List;
import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.transaction.annotation.Transactional;

import com.example.demo.user.SiteUser;

public interface courseRepository extends JpaRepository<course, Integer>{
    List<course> findByAuthor(SiteUser siteUser);

    List<course> findByIdAndAuthor(Integer id, SiteUser siteUser);

    @Transactional
    void deleteByIdAndAuthor(Integer id, SiteUser siteUser);

    
}
