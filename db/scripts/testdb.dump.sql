PGDMP                         x            testdb    12.2    12.2     h           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            i           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            j           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            k           1262    17994    testdb    DATABASE     v   CREATE DATABASE testdb WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.utf8' LC_CTYPE = 'en_US.utf8';
    DROP DATABASE testdb;
                postgres    false            �            1259    18000    users    TABLE     c   CREATE TABLE public.users (
    id bigint NOT NULL,
    username character varying(20) NOT NULL
);
    DROP TABLE public.users;
       public         heap    postgres    false            e          0    18000    users 
   TABLE DATA           -   COPY public.users (id, username) FROM stdin;
    public          postgres    false    202          �
           2606    18004    users users_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    202            e      x�3������2��J�K����� 2g     