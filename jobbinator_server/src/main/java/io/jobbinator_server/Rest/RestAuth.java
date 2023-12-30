package io.jobbinator_server.Rest;

import io.jobbinator_server.DTO.AuthDTO;

import io.jobbinator_server.DTO.SignUpDTO;
import io.jobbinator_server.Repositories.JobRepository;
import io.jobbinator_server.Services.AuthService;
import io.jobbinator_server.Services.db_services.JobService;
import jakarta.validation.Valid;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/auth")
@CrossOrigin
public class RestAuth {

    private final AuthService service;

    public RestAuth(AuthService service) {
        this.service = service;
    }
    @PostMapping("/signup")
    public ResponseEntity signUpUser(@RequestBody @Valid SignUpDTO dto){
        return service.signUpUser(dto);
    }
    @PostMapping("/login")
    public ResponseEntity loginUser(@RequestBody @Valid AuthDTO dto){
        return service.loginUser(dto);
    }
}
