-- Assuntos: Tipos Algébricos de Dados, Polimorfismo, Hierarquia de Classes

{- 1. Uma forma geométrica simples pode ser um círculo, quadrado, triângulo ou retângulo,
por exemplo. Podemos definir algumas alternativas pelo tipo:
data Forma = Circulo Float | Retangulo Float Float
que diz que há duas maneiras de construir um elemento “Forma”. Uma maneira é
fornecer o raio de um círculo; a outra alternativa é dar os lados de um retângulo.
a) Defina uma função para verificar se uma Forma é redonda ou não.
b) Defina uma única função para calcular a área de um círculo ou de um retângulo.
c) Responda: quais são os tipos dos construtores de dados “Circulo” e “Retangulo”?
d) Adicione um construtor de dados do tipo Triangulo, e estenda a função dos itens
a) e b) para incluir triângulos-}

data Forma = Circulo Float | Retangulo Float Float | Triangulo Float Float Float

redondo :: Forma -> Bool
redondo (Circulo _) = True
redondo (Retangulo _ _) = False
redondo (Triangulo _ _ _) = False

area :: Forma -> Float
area (Circulo raio) = pi * raio^2
area (Retangulo base altura) = base * altura
area (Triangulo a b c) =
  let s = (a + b + c) / 2
  in sqrt(s * (s - a) * (s - b) * (s - c)) -- Fórmula de Herão para a área do triângulo

{-C) Os tipos dos construtores de dados "Circulo" e "Retangulo" são Float e Float Float, respectivamente. 
Isso significa que o construtor "Circulo" recebe um valor Float (o raio) e "Retangulo" recebe dois valores 
Float (base e altura).-}

--2. Determine o tipo de cada função definida a seguir.
dobro :: Num a => a -> a
dobro x = x*2
aprovado :: (Ord a, Num a) => a -> Bool
aprovado nota = nota >= 6
myLog :: Floating a => a -> a -> a
myLog x b = log x / log b

{-3. Determine o tipo das expressões abaixo.
a) [[]]
b) [[10,20,30], [], [5,6], [24]]
c) (10e-2, 20e-2, 30e-3)
d) [(2,3), (4,5.6), (6,4.55)]
e) (["bom","dia","brasil"], sum, drop 7 "Velho mundo")
f) [sum, length]
-}

{-a)A expressão [[]] representa uma lista que contém uma lista vazia. Portanto, 
seu tipo é uma lista de listas vazias:
[[]] :: [[a]]-}
{-b)A expressão [[10,20,30], [], [5,6], [24]] representa uma lista que contém quatro listas diferentes, 
algumas das quais podem ser vazias e outras contendo elementos. Portanto, seu tipo é uma lista de listas de números:
[[10,20,30], [], [5,6], [24]] :: [[Int]]-}
{-c)A expressão (10e-2, 20e-2, 30e-3) representa uma tupla de três elementos, onde cada elemento é um número 
em ponto flutuante. Portanto, seu tipo é uma tupla de números em ponto flutuante:
(10e-2, 20e-2, 30e-3) :: (Floating a) => (a, a, a)-}
{-d)A expressão [(2,3), (4,5.6), (6,4.55)] representa uma lista de tuplas, onde cada tupla contém dois elementos. 
O primeiro elemento de cada tupla é um número inteiro, e o segundo elemento pode ser um número inteiro ou um número
em ponto flutuante. Portanto, seu tipo é uma lista de tuplas com o primeiro elemento sendo um Int e o segundo podendo 
ser Int ou Float: [(2,3), (4,5.6), (6,4.55)] :: [(Int, Num)]-}
{-e) A expressão (["bom","dia","brasil"], sum, drop 7 "Velho mundo") é uma tupla que contém três elementos: 
uma lista de strings, a função sum e o resultado da função drop 7 "Velho mundo". 
A lista de strings ["bom","dia","brasil"] tem tipo [String].
A função sum é uma função que opera em listas de números e retorna a soma desses números, 
portanto seu tipo é Num a => [a] -> a.
A função drop 7 "Velho mundo" é uma operação que remove os primeiros 7 caracteres da string "Velho mundo", 
então seu tipo é drop :: Int -> [a] -> [a] aplicada a uma string.
Portanto, o tipo da tupla é:
(["bom","dia","brasil"], sum, drop 7 "Velho mundo") :: ([String], Num a => [a] -> a, [Ch-}
{-f) A expressão [sum, length] é uma lista que contém duas funções: sum e length. 
A função sum é como discutido anteriormente, e a função length é uma função que calcula o comprimento de uma lista,
 então seu tipo é length :: [a] -> Int. Portanto, o tipo da lista é:
[sum, length] :: Num a => [[a]] -> [a] -> Int-}

{-4. Defina um novo tipo para representar uma coordenada cartesiana:
a) Usando a expressão type.
b) Usando a expressão data.
c) Defina uma função para somar duas coordenadas, usando o tipo que você definiu
no item a).
d) Defina uma função para somar duas coordenadas, usando o tipo que você definiu
no item b)-}

--a)
type CoordenadaCartesianaA = (Double, Double)
--b)
data CoordenadaCartesianaB = CoordenadaCartesianaB Double Double deriving Show
--c)
somaCoordA :: CoordenadaCartesianaA -> CoordenadaCartesianaA -> CoordenadaCartesianaA
somaCoordA (x1, y1) (x2, y2) = (x1 + x2, y1 + y2)
--d)
somaCoordB :: CoordenadaCartesianaB -> CoordenadaCartesianaB -> CoordenadaCartesianaB
somaCoordB (CoordenadaCartesianaB x1 y1) (CoordenadaCartesianaB x2 y2) = CoordenadaCartesianaB (x1 + x2) (y1 + y2)


