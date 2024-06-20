--Assunto: Cálculo Lambda

{-1. Determine o tipo e o valor das seguintes expressões que usam composição de funções
e expressões lambda:
a) (toUpper . head) ["maria","jose","silva"]
b) (not . odd . length) "felicidade"
c) (isLetter . head . head . reverse) ["maria","silva","pereira"]
d) (even . (\x -> x*2 + 3) . (\x -> div x 2) . snd) (9+4,9-4)-}

{-a) A expressão (toUpper . head) ["maria","jose","silva"] é uma composição de funções. 
Primeiro, a função head é aplicada à lista, retornando a cabeça da lista, que é a string "maria". 
Em seguida, a função toUpper é aplicada a essa string, convertendo-a para maiúsculas.
Tipo: String
Valor: "MARIA"
b) A expressão (not . odd . length) "felicidade" é uma composição de funções. 
Primeiro, a função length é aplicada à string, retornando o comprimento da string. 
Em seguida, a função odd é aplicada a esse comprimento, verificando se é ímpar. Por fim, a função not é aplicada ao resultado de odd, retornando o oposto do valor.
Tipo: Bool
Valor: False (porque o comprimento da string "felicidade" é 10, que não é ímpar)
c) A expressão (isLetter . head . head . reverse) ["maria","silva","pereira"] é uma composição de funções. 
Primeiro, a função reverse é aplicada à lista, revertendo a ordem das strings. 
Em seguida, a função head é aplicada a essa lista revertida, retornando a primeira string da lista original, 
que é "pereira". Depois, a função head é aplicada a essa string, retornando o primeiro caractere. 
Por fim, a função isLetter verifica se esse caractere é uma letra.
Tipo: Bool
Valor: True (porque o primeiro caractere da string "pereira" é uma letra)
d) A expressão (even . (\x -> x*2 + 3) . (\x -> div x 2) . snd) (9+4,9-4) é uma composição de funções. 
Primeiro, a função snd é aplicada à tupla (9+4,9-4), retornando o segundo elemento da tupla, que é 5. 
Em seguida, a função anônima (\x -> div x 2) é aplicada a esse valor, dividindo-o por 2. 
Depois, a função anônima (\x -> x*2 + 3) é aplicada ao resultado dessa divisão, multiplicando-o por 2 e adicionando 3. Por fim, a função even verifica se o resultado final é um número par.
Tipo: Bool
Valor: True (porque 5 * 2 + 3 = 13, que é ímpar, então a função even retorna False, 
mas a composição completa é not False, que é True)-}

{-2. Escreva uma função anônima que recebe uma tripla formada pelo nome, peso e altura
de uma pessoa e resulta no seu índice de massa corporal, 
dado pela razão entre o peso e o quadrado da altura da pessoa.-}

pessoa :: (String,Float,Float)
pessoa = ("Maria", 70.0, 1.75)

calcularIMC :: (a, Double, Double) -> Double
calcularIMC = (\(_, peso, altura) -> peso / (altura^2))

{-3. Escreva uma expressão para selecionar (filtrar) os elementos múltiplos de 3 em uma
lista de números. Utilize a função filter :: (a -> Bool) -> [a] -> [a] do prelúdio. Especifique
a função que determina a propriedade a ser satisfeita pelos elementos selecionados usando
uma expressão lambda.-}

lista :: [Integer]
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
multiplosDe3 :: [Integer]
multiplosDe3 = filter (\x -> x `mod` 3 == 0) lista

{-4. Defina a função composta que recebe duas funções como argumentos e resulta na
função composta das mesmas, (f ◦ g)(x) = f (g(x)). Use uma definição local (where) para
definir a função resultante.
a) Escreva outra definição para a função composta usando uma expressão lambda para
determinar o seu resultado. Nesta versão não use definições locais.
b) Determine o tipo mais geral da função composta.
c) Teste a função composta calculando o tipo e o valor da expressão
(composta even length) "linguagens modernas"
-}

--a)Definição da função composta usando uma definição local (where):
comp :: (b -> c) -> (a -> b) -> a -> c
comp f g x = f (g x)
--b) Definição da função composta usando uma expressão lambda:
comp2 :: (t1 -> t2) -> (t3 -> t1) -> t3 -> t2
comp2 f g x = f (g x)
--c) Tipo mais geral da função composta:
resultado :: Bool
resultado = comp even length "linguagens modernas"

{-5. Para cada uma das seguintes funções abaixo, que foram escritas usando seções de
operadores:
• determine o tipo mais geral da função
• reescreva a função usando expressões lambda
a) (‘c’:)
b) (:"fim")
c) (==2)
d) (++"\n")
e) (^3)
f) (3^)
g) (‘elem’ "AEIOU")-}
{-a) (‘c’:)

Tipo mais geral: (Num a) => [a] -> [Char]
Reescrita usando expressão lambda: \x -> 'c' : x
b) (:"fim")

Tipo mais geral: [Char] -> [Char]
Reescrita usando expressão lambda: \x -> x ++ "fim"
c) (==2)

Tipo mais geral: (Eq a, Num a) => a -> Bool
Reescrita usando expressão lambda: \x -> x == 2
d) (++"\n")

Tipo mais geral: [Char] -> [Char]
Reescrita usando expressão lambda: \x -> x ++ "\n"
e) (^3)

Tipo mais geral: (Num a, Integral b) => b -> a
Reescrita usando expressão lambda: \x -> x ^ 3
f) (3^)

Tipo mais geral: (Integral a, Num b) => a -> b
Reescrita usando expressão lambda: \x -> 3 ^ x
g) (‘elem’ "AEIOU")

Tipo mais geral: Char -> Bool
Reescrita usando expressão lambda: \x -> elem x "AEIOU"-}

{-6. Determine o valor da expressão:
let pares = [(1,8),(2,5),(0,1),(4,4),(3,2)]
h = sum . map (\(x,y) -> x*y-1) . filter (\(x,_) -> even x)
in h pares

Filtrando os pares pares, obtemos [(2,5),(4,4)].
Aplicando a expressão x*y-1 a esses pares, obtemos [9,15].
Somando esses valores, obtemos o resultado final: 9 + 15 = 24.
Portanto, o valor da expressão é 24.
-}
