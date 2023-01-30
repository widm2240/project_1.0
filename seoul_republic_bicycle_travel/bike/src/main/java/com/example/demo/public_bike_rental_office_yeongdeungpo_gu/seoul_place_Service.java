package com.example.demo.public_bike_rental_office_yeongdeungpo_gu;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class seoul_place_Service implements seoulService {
    @Autowired
    private seoul_place_Repository seoul_place_Repository;
    @Override
    public List<seoul_recommend_course_yeongdeungpo_gu> getAllplaces(){
        return seoul_place_Repository.findAll();
    }

}
