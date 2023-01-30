package com.example.demo.public_bike_rental_office_yeongdeungpo_gu;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import lombok.Getter;
import lombok.Setter;

@Entity
@Getter
@Setter
public class public_bike_rental_office_yeongdeungpo_gu {
    @Id
    private String Rental_Office_Number;
    
    @Column(name = "Rental_Office_Name_KOR")
    private String placename;

    // private String Rental_Office_Name_ENG;

    private String Ward_KOR;

    // private String Ward_ENG;

    // private String Address_KOR;

    // private String Address_ENG;

    private String Latitude;

    private String Longitude;

    private String Holder_LCD;

    private String Holder_QR;
}
