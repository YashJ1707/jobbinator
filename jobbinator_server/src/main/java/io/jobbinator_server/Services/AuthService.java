package io.jobbinator_server.Services;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.ObjectWriter;
import io.jobbinator_server.DTO.AuthDTO;
import io.jobbinator_server.DTO.SignUpDTO;
import io.jobbinator_server.Entities.User;
import io.jobbinator_server.Services.db_services.UserService;
import jakarta.security.auth.message.AuthException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;


@Service
public class AuthService {
    @Autowired
    private UserService service;
    public ResponseEntity<String> signUpUser(SignUpDTO dto){
        service.signupUser(dto);
        return ResponseEntity.ok("Signed up successfully");
    }
    public ResponseEntity<String> loginUser(AuthDTO dto){
        try {
            User user=service.loginUser(dto.getEmail(),dto.getHash());
            ObjectWriter ow=new ObjectMapper().writer().withDefaultPrettyPrinter();
            String response=ow.writeValueAsString(user);
            return ResponseEntity.ok().body(response);
        } catch (AuthException | JsonProcessingException e) {
            throw new RuntimeException(e);
        }
    }
}
