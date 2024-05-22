--
-- Database: `bubbolitas`
--
-- --------------------------------------------------------
--
-- Table structure for table `users`
--

DROP DATABASE if exists bubbolitas;
create database if not exists bubbolitas;
use bubbolitas;

CREATE TABLE `users` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `firstname` varchar(20) NOT NULL,
    `lastname` varchar(20) NOT NULL,
    `email` varchar(100) NOT NULL,
    `username` varchar(20) NOT NULL,
    `password` text NOT NULL,
    `address` text,
    `admin` BOOLEAN NOT NULL,
    `created_at` timestamp DEFAULT CURRENT_TIMESTAMP,
    `updated_at` timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX(id)
);

--
-- Dumping data for table `egg_groups`
--

INSERT INTO `users` (`id`, `firstname`, `lastname`, `email`, `username`, `password`, `address`, `admin`, `created_at`, `updated_at`) VALUES
(1, 'Guillaume', 'Eap', 'guillaume@gmail.com', 'franku', 'password123', '123 Main St, City, Country', TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(2, 'Quentin', 'Doulcet', 'quentin@gmail.com', 'kantun', 'password456', '456 Elm St, City, Country', FALSE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(3, 'Manel', 'Djedir', 'manel@gmail.com', 'manou', 'password456', '213 Elm St, City, Country', FALSE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(4, 'Admin', 'Admin', 'admin@gmail.com', 'admin', 'adminpassword', NULL, TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
    `id` int(11) NOT NULL,
    `name` varchar(70) NOT NULL,
    `description` text NOT NULL,
    `price` int(11) NOT NULL,
    `extras` text,
    `created_at`timestamp DEFAULT CURRENT_TIMESTAMP,
    `updated_at`timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX(id)
);

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`id`, `name`, `description`, `price`, `extras`, `created_at`, `updated_at`) VALUES
(1, 'Bubble Tea au Taro', 'Un délicieux bubble tea à base de taro et de perles de tapioca.', 5, 'Perles de tapioca', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(2, 'Bubble Tea à la Mangue', 'Un rafraîchissant bubble tea à la saveur tropicale de mangue.', 6, 'Popping boba à la mangue', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(3, 'Bubble Tea à la Fraise', "Un bubble tea fruité à la fraise, parfait pour l'été.", 12, 'Perles de tapioca, lait de coco', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(4, 'Bubble Tea au Matcha', "Un bubble tea riche en saveur, avec une touche d'amertume caractéristique du matcha japonais.", 6, "Perles de tapioca, lait d'amande", CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(5, 'Bubble Tea à la Noix de Coco', 'Un bubble tea exotique et crémeux, avec une note subtile de noix de coco.', 8, 'Perles de tapioca, lait de coco', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(6, 'Bubble Tea au Litchi', 'Un délicat bubble tea au parfum sucré et floral du litchi, parfait pour une pause rafraîchissante.', 7, 'Popping boba au litchi', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
(7, 'Bubble Tea au Thé Vert et Citron Vert', 'Une combinaison rafraîchissante de thé vert et de zeste de citron vert dans un bubble tea léger et revitalisant.', 6, 'Perles de tapioca, tranches de citron vert', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

-- --------------------------------------------------------
--
-- Table structure for table `orders`
--
CREATE TABLE `orders` (
    `id` int(11) NOT NULL,
    `valid` BOOLEAN,
    `quantity` int(11) NOT NULL,
    `total_price` int(11) NOT NULL,
    `created_at`timestamp DEFAULT CURRENT_TIMESTAMP,
    `updated_at`timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    `user_id` int(11), 
    `product_id` int(11)
);

ALTER TABLE `orders`
ADD FOREIGN KEY (`user_id`) REFERENCES `users`(`id`),
ADD FOREIGN KEY (`product_id`) REFERENCES `products`(`id`); 


--
-- Dumping data for table `items`
--

INSERT INTO `orders` (`id`, `valid`, `quantity`, `total_price`, `created_at`, `updated_at`, `user_id`, `product_id`) VALUES
(1, TRUE, 2, 50, '2024-04-16 12:00:00', '2024-04-16 12:00:00', 1, 1),
(2, FALSE, 1, 30, '2024-04-16 12:00:00', '2024-04-16 12:00:00', 2, 2),
(3, TRUE, 3, 75, '2024-04-16 12:00:00', '2024-04-16 12:00:00', 1, 3);

-- --------------------------------------------------------