-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  mer. 28 juil. 2021 à 10:33
-- Version du serveur :  10.4.10-MariaDB
-- Version de PHP :  7.4.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `grossiste`
--

-- --------------------------------------------------------

--
-- Structure de la table `produits`
--

DROP TABLE IF EXISTS `produits`;
CREATE TABLE IF NOT EXISTS `produits` (
  `produit_id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `description` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `quantite` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `ajouté on` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `prix` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`produit_id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Déchargement des données de la table `produits`
--

INSERT INTO `produits` (`produit_id`, `nom`, `description`, `quantite`, `ajouté on`, `prix`) VALUES
(2, 'Apla', 'Boisson Gazeuze', '7', '2021-02-20 21:10:59', '1850'),
(3, 'Brownies', 'Cake', '35', '2021-02-18 17:13:28', '700'),
(4, 'Ticket Orange', 'Ticket de recharge', '50', '2021-02-19 18:01:31', '1250'),
(5, 'Fromage 16 portions', 'Préparation alimentaire fromage', '50', '2021-02-19 18:04:33', '2100'),
(6, 'Biscuit Major', 'Biscuit', '65', '2021-02-19 18:06:30', '1250'),
(7, 'Fanta', 'Boisson Gazeuze', '30', '2021-02-21 07:50:10', '1900'),
(8, 'Chocolat Maestro Noisettes', 'Chocolat', '50', '2021-02-19 18:22:02', '1350'),
(9, '1 Kg. farine', 'Farine ', '80', '2021-02-19 18:26:39', '700'),
(10, '1 Kg. Sucre', 'Sucre', '50', '2021-02-19 18:34:16', '1000'),
(11, 'Ticket Telecom', 'Ticket De Rechage', '50', '2021-02-19 18:47:34', '1250'),
(12, 'Gaufrettes Saida', 'Gaufrettes', '100', '2021-02-19 18:57:06', '1000'),
(13, 'Eau Safia', 'Eau Minérale', '100', '2021-02-19 19:01:18', '700'),
(14, 'Eau Sabrine', 'Eau Minérale', '100', '2021-02-19 19:04:01', '700'),
(15, 'Eau Cristaline', 'Eau Minérale', '48', '2021-07-13 21:17:41', '700');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
