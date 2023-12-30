package io.jobbinator_server;

import jakarta.security.auth.message.AuthException;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.context.request.WebRequest;


@ControllerAdvice
public class ExceptionController {
     @ExceptionHandler(AuthException.class)
    public ResponseEntity<Object> handleAuthExceptions(AuthException exception, WebRequest webRequest){
         return new ResponseEntity<Object>(exception.getMessage(), new HttpHeaders(),HttpStatus.UNAUTHORIZED);
     }
    @ExceptionHandler(UsernameNotFoundException.class)
    public ResponseEntity<Object> handleUsernameNotFoundExceptions(UsernameNotFoundException exception, WebRequest webRequest){
        return new ResponseEntity<Object>(exception.getMessage(), new HttpHeaders(),HttpStatus.NOT_FOUND);
    }

}

