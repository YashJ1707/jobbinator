package io.jobbinator_server.Services.db_services;

import io.jobbinator_server.DTO.SignUpDTO;
import io.jobbinator_server.Entities.User;
import io.jobbinator_server.Repositories.UserRepository;
import jakarta.security.auth.message.AuthException;
import jakarta.transaction.Transactional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import java.util.Objects;

@Service
@Transactional
public class UserService {

    @Autowired
    private UserRepository userRepo;

    public void signupUser(SignUpDTO dto){
        User user= User.builder().age(dto.getAge()).dob(dto.getDob()).name(dto.getName()).number(dto.getNumber()).gender(dto.getGender()).hash(dto.getHash()).email(dto.getEmail()).build();
        userRepo.save(user);
    }
    public User loginUser(String email, String hash) throws AuthException {

        User user=userRepo.findByEmail(email);
        if(user==null){
            throw new UsernameNotFoundException("User not found");
        }
        String userHash=user.getHash();
        if(!Objects.equals(hash, userHash)){
            throw new AuthException("Invalid Credentials!");
        }
        return user;
    }
}
