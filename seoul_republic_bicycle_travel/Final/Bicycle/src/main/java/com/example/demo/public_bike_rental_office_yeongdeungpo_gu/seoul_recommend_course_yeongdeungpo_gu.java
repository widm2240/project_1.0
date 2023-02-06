package com.example.demo.public_bike_rental_office_yeongdeungpo_gu;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import lombok.Getter;
import lombok.Setter;

@Entity
@Getter
@Setter
public class seoul_recommend_course_yeongdeungpo_gu {
    @Id
    private String Designation;

    private String Address;

    private String Latitude;

    private String Longitude;


}
