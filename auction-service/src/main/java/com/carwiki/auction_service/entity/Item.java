package com.carwiki.auction_service.entity;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.util.UUID;


@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "items")
public class Item {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    private UUID id;

    @Column(nullable = false)
    private String make;
    @Column(nullable = false)
    private String model;

    private Integer year;

    @Column(nullable = false)
    private String color;
    private Integer mileage;

    @Column(nullable = false)
    private String imageUrl;

    @OneToOne
    @MapsId
    @JoinColumn(name = "auction_id")
    private Auction auction;


}
