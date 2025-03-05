package com.carwiki.auction_service.entity;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import org.hibernate.annotations.ColumnDefault;
import org.springframework.data.annotation.CreatedDate;
import org.springframework.data.annotation.LastModifiedDate;

import java.time.LocalDateTime;
import java.util.UUID;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Entity
public class Auction {
    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    private UUID id;


    private String seller = "Mandalay";

    private String winner;

    @Column(name="reserve_price")
    @ColumnDefault("0")
    private Integer reservePrice;

    private Integer highestBid;
    private Integer soldAmount;

    @Column(name = "created_at", nullable = false, updatable = false)
    private LocalDateTime createdAt;

    @Column(name = "updated_at", nullable = false)
    private LocalDateTime updatedAt;

    @Column( name = "auction_end", nullable = false)
    private  LocalDateTime auctionEnd;


    private Status status = Status.LIVE;

    @OneToOne(mappedBy = "auction", cascade = CascadeType.ALL)
    private Item item;


    public boolean hasReservePrice() {
        return reservePrice > 0;
    }
}
