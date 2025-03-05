package com.carwiki.auction_service.dto;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.time.LocalDateTime;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class CreateAuctionDto {
    private String make;
    private String model;
    private String color;
    private Integer year;
    private Integer mileage;
    private String imageUrl;
    private Integer reservePrice;
    private LocalDateTime auctionEnd;

}
