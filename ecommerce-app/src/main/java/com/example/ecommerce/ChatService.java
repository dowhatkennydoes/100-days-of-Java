package com.example.ecommerce;

import java.util.HashMap;
import java.util.Map;

import org.springframework.stereotype.Service;

@Service
public class ChatService {
    private final Map<String, String> predefined;

    public ChatService() {
        predefined = new HashMap<>();
        predefined.put("hello", "Hello! How can I assist you today?");
        predefined.put("hi", "Hi there! What can I do for you?");
        predefined.put("help", "Sure, I'm here to help with your shopping needs.");
    }

    public String respond(String message) {
        if (message == null) {
            return "I didn't quite get that.";
        }
        String lower = message.toLowerCase();
        return predefined.entrySet().stream()
                .filter(e -> lower.contains(e.getKey()))
                .map(Map.Entry::getValue)
                .findFirst()
                .orElse("Sorry, I can only answer basic greetings.");
    }
}
