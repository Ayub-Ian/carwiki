package com.carwiki.auction_service.repository;

import com.carwiki.auction_service.entity.Item;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.UUID;

public interface ItemRepository extends JpaRepository<Item, UUID> {
}
