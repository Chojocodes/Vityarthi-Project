# Project: Student Course Enrollment Analyzer

## Problem statement
Educational administrators and course coordinators often struggle to manually track student enrollments across multiple overlapping courses. Without automated tools, it is time-consuming and error-prone to identify shared student populations, find students taking only one specific subject, and ensure every unique student is assigned a standardized roll number for administrative tracking and grading.

## Scope of the project
This project provides a lightweight, Python-based utility script that automates the analysis of course enrollment data using mathematical set operations. The scope includes processing basic data structures (like tuples or lists) of enrolled students for courses (such as Python and Java). It handles extracting specific enrollment overlaps, generating sequential roll numbers for all unique students starting from a defined base (e.g., 101), and programmatically validating whether student cohorts are completely distinct.

## Target users
*   University Administrators and Registrars
*   Course Coordinators and Department Heads
*   Academic Advisors 
*   Educators and Instructors managing multiple class rosters

## High-level features
*   **Overlap Detection:** Identifies students concurrently enrolled in multiple specified courses (utilizing Set Intersection).
*   **Master Roster Compilation:** Creates a comprehensive list of all unique students across the given courses (utilizing Set Union).
*   **Exclusive Enrollment Tracking:** Isolates students who are enrolled in only one of the two specified courses (utilizing Symmetric Difference).
*   **Automated Roll Number Assignment:** Generates a dictionary that automatically assigns sequential, unique roll numbers to alphabetically sorted students.
*   **Disjoint Cohort Validation:** Automatically checks and returns a boolean value indicating whether two course groups are completely independent with no shared students.