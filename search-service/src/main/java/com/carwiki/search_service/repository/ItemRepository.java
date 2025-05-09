package com.carwiki.search_service.repository;

import com.carwiki.search_service.entity.Item;
import org.springframework.data.mongodb.repository.MongoRepository;

import java.time.LocalDateTime;
import java.util.Optional;

public interface ItemRepository extends MongoRepository<Item, String> {
}
