# Blog Project

## Overview

This web application provides a platform for users to create and manage blog posts, categories, and comments. It uses Django Rest Framework for the backend and Vue.js for the frontend.

## Architecture

### Database

![challange-blog (4)](https://github.com/user-attachments/assets/c18dbd59-cf03-4a1a-8dce-995d34850031)

The database schema consists of the following tables:

#### `user`
- `id` (INTEGER, Primary Key, Auto Increment)
- `email` (VARCHAR, Unique)
- `last_login` (DATETIME)
- `is_staff` (BOOL)
- `is_active` (BOOL)
- `is_superuser` (BOOL)
- `avatar` (VARCHAR)
- `password` (VARCHAR)
- `person_id` (INTEGER, FK for `person.id`)
- `created_at` (DATETIME)
- `updated_at` (DATETIME)

#### `person`
- `id` (INTEGER, Primary Key, Auto Increment)
- `name` (VARCHAR)
- `created_at` (DATETIME)
- `updated_at` (DATETIME)

#### `post`
- `id` (INTEGER, Primary Key, Auto Increment)
- `title` (VARCHAR)
- `content` (TEXT)
- `author_id` (INTEGER, FK for `user.id`)
- `status` (VARCHAR)
- `category_id` (INTEGER, FK for `categorie.id`)
- `created_at` (DATETIME)
- `updated_at` (DATETIME)

#### `category`
- `id` (INTEGER, Primary Key, Auto Increment)
- `name` (VARCHAR)
- `created_at` (DATETIME)
- `updated_at` (DATETIME)

#### `comment`
- `id` (INTEGER, Primary Key, Auto Increment)
- `user_id`  (INTEGER, FK for `user.id`)
- `description` (TEXT)
- `post_id` (INTEGER, FK for `post.id`)
- `created_at` (DATETIME)
- `updated_at` (DATETIME)
