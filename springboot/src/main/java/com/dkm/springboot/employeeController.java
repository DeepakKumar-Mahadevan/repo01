package com.dkm.springboot;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/employees")
public class employeeController {
    private final employeeRepository employeeRepository;

    public employeeController(employeeRepository employeeRepository) {
        this.employeeRepository = employeeRepository;
    }

    @GetMapping
    public List<employee> getAllemployees() {
        return employeeRepository.findAll();
    }

    @PostMapping
    public employee createemployee(@RequestBody employee employee) {
        return employeeRepository.save(employee);
    }

    @GetMapping("/{id}")
    public ResponseEntity<employee> getemployeeById(@PathVariable("id") Long id) {
        Optional<employee> optionalemployee = employeeRepository.findById(id);
        if (optionalemployee.isPresent()) {
            return ResponseEntity.ok(optionalemployee.get());
        } else {
            return ResponseEntity.notFound().build();
        }
    }

    @PutMapping("/{id}")
    public ResponseEntity<employee> updateemployee(@PathVariable("id") Long id, @RequestBody employee updatedemployee) {
        Optional<employee> optionalemployee = employeeRepository.findById(id);
        if (optionalemployee.isPresent()) {
            employee employee = optionalemployee.get();
            employee.setName(updatedemployee.getName());
            employee.setEmail(updatedemployee.getEmail());
            employeeRepository.save(employee);
            return ResponseEntity.ok(employee);
        } else {
            return ResponseEntity.notFound().build();
        }
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteemployee(@PathVariable("id") Long id) {
        Optional<employee> optionalemployee = employeeRepository.findById(id);
        if (optionalemployee.isPresent()) {
            employeeRepository.deleteById(id);
            return ResponseEntity.noContent().build();
        } else {
            return ResponseEntity.notFound().build();
        }
    }
}
