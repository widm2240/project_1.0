package com.example.demo.public_bike_rental_office_yeongdeungpo_gu;



import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;







public interface rental_office_Repository extends JpaRepository<public_bike_rental_office_yeongdeungpo_gu, String> {
    List<public_bike_rental_office_yeongdeungpo_gu>findByplacenameContaining(String keyword);
}
