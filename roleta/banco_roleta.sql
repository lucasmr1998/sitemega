-- ============================================================
-- Banco de Dados: u635775069_megalink (Hostinger)
-- Importe este arquivo via phpMyAdmin no banco já existente
-- NÃO inclui CREATE DATABASE — use o banco criado na Hostinger
-- ============================================================

SET NAMES utf8mb4;
SET time_zone = '-03:00';

-- ------------------------------------------------------------
-- Tabela: usuarios
-- Registra cada participante que girou a roleta
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `usuarios` (
  `ID`                 INT(11)       NOT NULL AUTO_INCREMENT,
  `nome`               VARCHAR(255)  NOT NULL,
  `cpf`                VARCHAR(20)   NOT NULL,
  `email`              VARCHAR(255)  DEFAULT NULL,
  `telefone`           VARCHAR(30)   DEFAULT NULL,
  `cep`                VARCHAR(10)   DEFAULT NULL,
  `endereco`           VARCHAR(255)  DEFAULT NULL,
  `bairro`             VARCHAR(100)  DEFAULT NULL,
  `cidade`             VARCHAR(100)  DEFAULT NULL,
  `estado`             VARCHAR(10)   DEFAULT NULL,
  `premio`             VARCHAR(255)  DEFAULT NULL,
  `canal_origem`       VARCHAR(50)   DEFAULT NULL,
  `status`             VARCHAR(50)   NOT NULL DEFAULT 'reservado',
  `responsavel_status` VARCHAR(100)  DEFAULT NULL,
  `data_giro`          DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `uq_cpf` (`cpf`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ------------------------------------------------------------
-- Tabela: premios
-- Estoque de prêmios por localidade
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `premios` (
  `id`         INT(11)      NOT NULL AUTO_INCREMENT,
  `premio`     VARCHAR(255) NOT NULL,
  `quantidade` INT(11)      NOT NULL DEFAULT 0,
  `localidade` VARCHAR(50)  NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ------------------------------------------------------------
-- Tabela: logs
-- Registra ações dos atendentes na área admin
-- ------------------------------------------------------------
CREATE TABLE IF NOT EXISTS `logs` (
  `id`          INT(11)      NOT NULL AUTO_INCREMENT,
  `responsavel` VARCHAR(100) DEFAULT NULL,
  `acao_nova`   VARCHAR(100) DEFAULT NULL,
  `acao_antiga` VARCHAR(100) DEFAULT NULL,
  `aonde`       VARCHAR(255) DEFAULT NULL,
  `data_acao`   DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ============================================================
-- Dados iniciais: prêmios por localidade
-- Os nomes DEVEM ser exatamente iguais ao que o código PHP usa
-- Ajuste as quantidades conforme sua necessidade
-- ============================================================

INSERT INTO `premios` (`premio`, `quantidade`, `localidade`) VALUES
-- Rio Grande
('desconto 60 reais',                       20, 'rio grande'),
('50% de desconto na taxa de instalação',   20, 'rio grande'),
('desconto 120 reais',                      20, 'rio grande'),
('1 mês de internet grátis',                20, 'rio grande'),
('Taxa de instalação grátis',               20, 'rio grande'),
('2 meses de internet grátis',              10, 'rio grande'),
('3 meses de internet grátis',               5, 'rio grande'),

-- Cassino
('desconto 60 reais',                       20, 'cassino'),
('50% de desconto na taxa de instalação',   20, 'cassino'),
('desconto 120 reais',                      20, 'cassino'),
('1 mês de internet grátis',                20, 'cassino'),
('Taxa de instalação grátis',               20, 'cassino'),
('2 meses de internet grátis',              10, 'cassino'),
('3 meses de internet grátis',               5, 'cassino'),

-- Pelotas
('desconto 60 reais',                       20, 'pelotas'),
('50% de desconto na taxa de instalação',   20, 'pelotas'),
('desconto 120 reais',                      20, 'pelotas'),
('1 mês de internet grátis',                20, 'pelotas'),
('Taxa de instalação grátis',               20, 'pelotas'),
('2 meses de internet grátis',              10, 'pelotas'),
('3 meses de internet grátis',               5, 'pelotas'),

-- São José do Norte
('desconto 60 reais',                       20, 'sjn'),
('50% de desconto na taxa de instalação',   20, 'sjn'),
('desconto 120 reais',                      20, 'sjn'),
('1 mês de internet grátis',                20, 'sjn'),
('Taxa de instalação grátis',               20, 'sjn'),
('2 meses de internet grátis',              10, 'sjn'),
('3 meses de internet grátis',               5, 'sjn');
