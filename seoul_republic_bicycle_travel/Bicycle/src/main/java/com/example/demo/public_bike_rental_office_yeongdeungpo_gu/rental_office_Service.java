package com.example.demo.public_bike_rental_office_yeongdeungpo_gu;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;


@Service
public class rental_office_Service implements rentalService{
    @Autowired 
    private rental_office_Repository rental_office_Repository;

    @Override
    public List<public_bike_rental_office_yeongdeungpo_gu> getAllrental() {
        return rental_office_Repository.findAll(); // 4
    }
    @Override
    public List<public_bike_rental_office_yeongdeungpo_gu> getplace(String keyword) {
        return rental_office_Repository.findByplacenameContaining(keyword); // 4
    }
}
