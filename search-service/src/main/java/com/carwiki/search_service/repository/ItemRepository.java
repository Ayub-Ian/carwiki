package com.carwiki.search_service.repository;

import com.carwiki.search_service.entity.Item;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface ItemRepository extends MongoRepository<Item, String> {
}
