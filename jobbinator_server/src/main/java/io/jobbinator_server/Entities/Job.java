package io.jobbinator_server.Entities;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "Jobs")
@Getter
@Setter
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class Job {
    @Id
    @GeneratedValue(strategy= GenerationType.IDENTITY)
    private Long id;
    @Column(name = "company_name", nullable = false)
    private String company;
    @Column(name = "job_title", nullable = false)
    private String title;
    @Column(name = "date_posted", nullable = false)
    private String datePosted;
    private String salary;
    private String tags;
    private String job_location;
    @Column(name = "job_description", nullable = false,length = 1000000)
    private String jobDescription;
    @Column(unique=true,length = 1000)
    private String url;
    private String website;
}