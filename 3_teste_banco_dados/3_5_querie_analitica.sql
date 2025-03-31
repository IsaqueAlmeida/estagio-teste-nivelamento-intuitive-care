-- 3.5 - Consultas SQL para análise dos dados

-- Total de operadoras por estado
SELECT uf, COUNT(*) AS total_operadoras 
FROM operadoras_saude 
GROUP BY uf 
ORDER BY total_operadoras DESC;

-- Receita total por operadora
SELECT o.nome_fantasia, SUM(d.receita) AS receita_total 
FROM demonstracoes_contabeis d
JOIN operadoras_saude o ON d.registro_ans = o.registro_ans
GROUP BY o.nome_fantasia 
ORDER BY receita_total DESC;

-- Demonstrativo financeiro por operadora
SELECT o.nome_fantasia, d.competencia, d.receita, d.despesa, d.resultado, d.patrimonio_liquido 
FROM demonstracoes_contabeis d
JOIN operadoras_saude o ON d.registro_ans = o.registro_ans
ORDER BY o.nome_fantasia, d.competencia;

-- 10 operadoras com maiores despesas no último trimestre
SELECT o.nome_fantasia, d.competencia, d.despesa 
FROM demonstracoes_contabeis d
JOIN operadoras_saude o ON d.registro_ans = o.registro_ans
WHERE d.competencia IN ('4T2024', '3T2024', '2T2024') 
ORDER BY d.despesa DESC 
LIMIT 10;

-- 10 operadoras com maiores despesas no último ano
SELECT o.nome_fantasia, SUM(d.despesa) AS total_despesa 
FROM demonstracoes_contabeis d
JOIN operadoras_saude o ON d.registro_ans = o.registro_ans
WHERE d.competencia LIKE '%2024' 
GROUP BY o.nome_fantasia 
ORDER BY total_despesa DESC 
LIMIT 10;
