package com.example.ecommerce;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
@RequestMapping("/products")
public class ProductController {
    @Autowired
    private ProductRepository repository;

    @GetMapping
    public String list(@RequestParam(value = "search", required = false) String search, Model model) {
        List<Product> products;
        if (search == null || search.isBlank()) {
            products = repository.findAll();
        } else {
            products = repository.findByNameContainingIgnoreCase(search);
        }
        model.addAttribute("products", products);
        model.addAttribute("search", search);
        return "products";
    }

    @PostMapping
    public String add(@ModelAttribute Product product) {
        repository.save(product);
        return "redirect:/products";
    }

    @PostMapping("/delete/{id}")
    public String delete(@PathVariable Long id) {
        repository.deleteById(id);
        return "redirect:/products";
    }

    @GetMapping("/api")
    @ResponseBody
    public List<Product> api(@RequestParam(value = "search", required = false) String search) {
        if (search == null || search.isBlank()) {
            return repository.findAll();
        }
        return repository.findByNameContainingIgnoreCase(search);
    }
}
