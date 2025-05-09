package com.carwiki.search_service.entity;

import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.index.Indexed;
import org.springframework.data.mongodb.core.index.TextIndexed;
import org.springframework.data.mongodb.core.mapping.Document;

import java.time.LocalDateTime;

@Data
@Document
public class Item {
    @Id
    private  String id;
    @Indexed
    private  String seller;
    private String winner;
    @TextIndexed
    private String make;
    @TextIndexed
    private String model;
    private Integer year;
    private String color;
    private Integer mileage;
    private String imageUrl;
    private  String status;
    private Integer reservePrice;
    private Integer soldAmount;
    private Integer currentHighBid;
    private LocalDateTime createdAt;
    @Indexed
    private LocalDateTime updatedAt;
    @Indexed
    private LocalDateTime auctionEnd;
}

