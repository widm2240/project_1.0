package com.example.demo.public_bike_rental_office_yeongdeungpo_gu;

import java.util.List;

public interface rentalService {
    List<public_bike_rental_office_yeongdeungpo_gu> getAllrental();
    List<public_bike_rental_office_yeongdeungpo_gu> getplace(String keyword);
}
