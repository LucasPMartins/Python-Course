type StudentId = Int
type FirstName = String
type LastName = String
type Age = Int

data Student = Student
    { studentId :: StudentId
    , firstName :: FirstName
    , lastName :: LastName
    , age :: Age
    } deriving (Show, Eq)

type Database = [Student]

initialDatabase :: Database
initialDatabase = []

adicionarEstudande :: Database -> Student -> Database
adicionarEstudande db student = student : db

encontrarEstudantePorID :: Database -> StudentId -> Maybe Student
encontrarEstudantePorID [] _ = Nothing
encontrarEstudantePorID (student:students) id
    | studentId student == id = Just student
    | otherwise = encontrarEstudantePorID students id

atualizarEstudantePorID :: Database -> StudentId -> Student -> Database
atualizarEstudantePorID db id newStudent =
    map (\student -> if studentId student == id then newStudent else student) db

filterEstudantePorID :: Database -> StudentId -> [Student]
filterEstudantePorID db id = filter (\student -> studentId student == id) db

printEstudantesFilterID :: Database -> StudentId -> IO ()
printEstudantesFilterID db id = do
    let filteredStudents = filterEstudantePorID db id
    if null filteredStudents
        then putStrLn "\nNenhum estudante encontrado com este ID."
        else do
            putStrLn "\nEstudantes encontrados com este ID:"
            mapM_ print filteredStudents

printBDAtualizada :: Database -> IO ()
printBDAtualizada db = do
    putStrLn "\nBanco de dados atualizado:"
    print db
    putStrLn ""

menu :: Database -> IO ()
menu db = do

    putStrLn "1 - Adicionar estudante"
    putStrLn "2 - Recuperar estudante por ID"
    putStrLn "3 - Atualizar informações do estudante"
    putStrLn "4 - Filtrar estudantes por ID"
    putStrLn "5 - Mostrar lista de estudantes"
    putStrLn "0 - Sair\n"
    putStr "Escolha uma opção:"
    opcao <- getLine
    putStrLn ""

    case opcao of
        "1" -> do
            putStrLn "---=== Adicionar Estudante ===---\n"
            putStr "Digite o ID do estudante:"
            studentId <- readLn
            putStr "Digite o primeiro nome do estudante:"
            firstName <- getLine
            putStr "Digite o sobrenome do estudante:"
            lastName <- getLine
            putStr "Digite a idade do estudante:"
            age <- readLn
            let newStudent = Student studentId firstName lastName age
                updatedDb = adicionarEstudande db newStudent
            putStrLn "\nEstudante adicionado com sucesso!"
            printBDAtualizada updatedDb
            menu updatedDb

        "2" -> do
            putStrLn "---=== Procurar Estudante ===---\n"
            putStr "Digite o ID do estudante:"
            studentId <- readLn
            case encontrarEstudantePorID db studentId of
                Just student -> do
                    putStrLn "\nEstudante encontrado:"
                    print student
                    putStrLn ""
                Nothing -> putStrLn "\nEstudante não encontrado."
            menu db

        "3" -> do
            putStrLn "---=== Atualizar Estudante ===---\n"
            putStr "Digite o ID do estudante que deseja atualizar:"
            studentId <- readLn
            case encontrarEstudantePorID db studentId of
                Just oldStudent -> do
                    putStr "Digite o novo primeiro nome do estudante:"
                    newFirstName <- getLine
                    putStr "Digite o novo sobrenome do estudante:"
                    newLastName <- getLine
                    putStr "Digite a nova idade do estudante:"
                    newAge <- readLn
                    let updatedStudent = oldStudent { firstName = newFirstName, lastName = newLastName, age = newAge }
                        updatedDb = atualizarEstudantePorID db studentId updatedStudent
                    putStrLn "\nInformações do estudante atualizadas com sucesso!"
                    printBDAtualizada updatedDb
                    menu updatedDb
                Nothing -> do
                    putStrLn "\nEstudante não encontrado."
                    menu db

        "4" -> do
            putStrLn "---=== Filtrar Estudantes ===---\n"
            putStr "Digite o ID do estudante para filtrar:"
            studentId <- readLn
            printEstudantesFilterID db studentId
            putStrLn ""
            menu db

        "5" -> do
            putStrLn "---=== Lista de Estudantes ===---"
            printBDAtualizada db
            menu db

        "0" -> putStrLn "\nEncerrando o programa..."

        _ -> do
            putStrLn "\nOpção inválida. Por favor, escolha uma opção válida.\n"
            menu db

main :: IO ()
main = do
    putStrLn "\nBem-vindo ao sistema de gerenciamento de estudantes!\n"
    menu initialDatabase
