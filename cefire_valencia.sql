-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: mysql
-- Tiempo de generación: 19-11-2020 a las 20:16:32
-- Versión del servidor: 8.0.20
-- Versión de PHP: 7.4.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `cefire_valencia`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cefire`
--

CREATE TABLE `cefire` (
  `id_a` bigint UNSIGNED NOT NULL,
  `data` date NOT NULL,
  `inici` time NOT NULL,
  `fi` time NOT NULL,
  `id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `compensa`
--

CREATE TABLE `compensa` (
  `id_a` bigint UNSIGNED NOT NULL,
  `data` date NOT NULL,
  `inici` time NOT NULL,
  `fi` time NOT NULL,
  `id` int NOT NULL,
  `motiu` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `curs`
--

CREATE TABLE `curs` (
  `id_a` bigint NOT NULL,
  `data` date NOT NULL,
  `inici` time NOT NULL,
  `fi` time NOT NULL,
  `curs` varchar(255) NOT NULL,
  `id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `guardia`
--

CREATE TABLE `guardia` (
  `id_a` bigint UNSIGNED NOT NULL,
  `data` date NOT NULL,
  `inici` time NOT NULL,
  `fi` time NOT NULL,
  `id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `lectura_rfid`
--

CREATE TABLE `lectura_rfid` (
  `id` bigint UNSIGNED NOT NULL,
  `lectura` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `data` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Disparadores `lectura_rfid`
--
DELIMITER $$
CREATE TRIGGER `Copia` AFTER INSERT ON `lectura_rfid` FOR EACH ROW INSERT INTO `cefire` (`id_a`, `data`, `inici`, `fi`, `id`) VALUES (NEW.id, CURRENT_DATE, CURRENT_TIME, CURRENT_TIME, NULL)
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `permis`
--

CREATE TABLE `permis` (
  `id_a` bigint UNSIGNED NOT NULL,
  `data` date NOT NULL,
  `inici` time NOT NULL,
  `fi` time NOT NULL,
  `id` int NOT NULL,
  `motiu` varchar(255) NOT NULL,
  `arxiu` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` bigint UNSIGNED NOT NULL,
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `email_verified_at` timestamp NULL DEFAULT NULL,
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `remember_token` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `Perfil` int NOT NULL DEFAULT '0',
  `rfid` varchar(12) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `visita`
--

CREATE TABLE `visita` (
  `id_a` bigint UNSIGNED NOT NULL,
  `data` date NOT NULL,
  `inici` time NOT NULL,
  `fi` time NOT NULL,
  `id` int NOT NULL,
  `centre` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cefire`
--
ALTER TABLE `cefire`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `compensa`
--
ALTER TABLE `compensa`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `curs`
--
ALTER TABLE `curs`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `guardia`
--
ALTER TABLE `guardia`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `lectura_rfid`
--
ALTER TABLE `lectura_rfid`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `permis`
--
ALTER TABLE `permis`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_email_unique` (`email`);

--
-- Indices de la tabla `visita`
--
ALTER TABLE `visita`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cefire`
--
ALTER TABLE `cefire`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1493;

--
-- AUTO_INCREMENT de la tabla `compensa`
--
ALTER TABLE `compensa`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=203;

--
-- AUTO_INCREMENT de la tabla `curs`
--
ALTER TABLE `curs`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=433;

--
-- AUTO_INCREMENT de la tabla `guardia`
--
ALTER TABLE `guardia`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=383;

--
-- AUTO_INCREMENT de la tabla `lectura_rfid`
--
ALTER TABLE `lectura_rfid`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=66;

--
-- AUTO_INCREMENT de la tabla `permis`
--
ALTER TABLE `permis`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=91;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=196;

--
-- AUTO_INCREMENT de la tabla `visita`
--
ALTER TABLE `visita`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1065;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
