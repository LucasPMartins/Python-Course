import Data.Char (toUpper)
import Data.Char (isAlpha)

-- Assuntos: Funções de Ordem Superior, Funções Genéricas sobre Listas.

{-1. Escreva as funções a seguir utilizando a função de ordem superior map:
a) Função primeiros :: [(a,b)] -> [a] que extrai o primeiro elemento de cada tupla-2 dentro
de uma lista. Dica: use a função fst.
b) Função maiusculas :: String -> String que converte uma string para outra string com
letras maiúsculas. Dica: utilize a função toUpper da biblioteca Data.Char.
c) Função dobros::Num a => [a] -> [a] que dobra todos os elementos de uma lista.-}

--a)
primeiros :: [(a, b)] -> [a]
primeiros lista = map fst lista
--b)
maiusculas :: String -> String
maiusculas str = map toUpper str
--c)
dobros :: Num a => [a] -> [a]
dobros lista = map (* 2) lista

{-2. Escreva as funções a seguir utilizando a função de ordem superior filter:
a) Função pares :: [Int] -> [Int] que remove todos os elementos ímpares de uma lista.
Dica: use a função even.
b) Função alfa :: String -> String que remove todos os caracteres não-alfabéticos de
uma string. Dica: utilize a função isAlpha da biblioteca Data.Char.
c) Defina a função rm_char :: Char -> String -> String que remove todas as ocorrências
de um caractere em uma string.
-}

--a)
pares :: [Int] -> [Int]
pares lista = filter even lista
--b)
alfa :: String -> String
alfa str = filter isAlpha str
--c)
rm_char :: Char -> String -> String
rm_char char str = filter (/= char) str


{-Escreva as funções a seguir utilizando a função de ordem superior foldr:
a) Função produto :: Num a => [a] -> a que computa o produto dos números de uma
lista.
b) Função e_logico :: [Bool] -> Bool que “e lógico” de todos os itens em uma lista.
c) Função concatena :: [String] -> String que junta uma lista de strings em uma única
string-}

--a)
produto :: Num a => [a] -> a
produto lista = foldr (*) 1 lista
--b)
e_logico :: [Bool] -> Bool
e_logico lista = foldr (&&) True lista
--c)
concatena :: [String] -> String
concatena lista = foldr (++) "" lista

