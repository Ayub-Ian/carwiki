package com.carwiki.auction_service.repository;

import com.carwiki.auction_service.entity.Auction;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

public interface AuctionRepository extends JpaRepository<Auction, UUID> {

    @Query("SELECT a FROM Auction a JOIN FETCH a.item")
    List<Auction> findAllWithItems();

    @Query("SELECT a FROM Auction a JOIN FETCH a.item WHERE a.id = :id")
    Optional<Auction> findByIdWithItem(@Param("id") UUID id);
}
