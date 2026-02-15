import random
import os
import time
import turtle

# გლობალური ცვლადები
HISTORY_FILE = "game_history.txt"
WORDS_FILE = "words.txt"
writer = None # ცვლადი ტექსტის დასაწერად
player_turtles = {} # თითოეული მოთამაშის კუ
player_start_x = {} # თითოეული მოთამაშის პოზიცია X ღერძზე

def init_visuals(players):
    global writer, player_turtles, player_start_x
    # --- TURTLE კონფიგურაცია
    try:
        # ფანჯრის და ყველა კუს სრული გადატვირთვა
        turtle.clearscreen() 
        turtle.bgcolor("white") 
        
        # კონფიგურაცია
        turtle.hideturtle()
        turtle.speed(3)
        turtle.pensize(5)
        turtle.title("Hangman - Multi Player Mode")
        
        #  ინიციალიზაცია (ტექსტი)
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.speed(0)
        writer.color("black")
        writer.goto(0, -180)
        
        # ინიციალიზაცია (მოთამაშეები)
        player_turtles = {}
        player_start_x = {}
        
        # ვიღებთ მაქსიმუმ 3 მოთამაშეს ვიზაულიზაციისთვის
        visual_players = players[:3] 
        count = len(visual_players)
        
        positions = []
        if count == 1: positions = [0]
        elif count == 2: positions = [-150, 150]
        else: positions = [-200, 0, 200]
        
        for i, p in enumerate(visual_players):
            x = positions[i]
            player_start_x[p] = x
            
            t = turtle.Turtle()
            t.hideturtle()
            t.speed(0) 
            t.pensize(3)
            t.color("black")
            
            # სახელის დაწერა თავზე
            t.penup()
            t.goto(x, 100)
            t.write(p, align="center", font=("Arial", 10, "bold"))
            
            player_turtles[p] = t
            
    except Exception as e:
        print(f"Visual init warning: {e}")

def update_visual_word(text):
    # განახლება ეკრანზე
    pass


def draw_hangman_part(player_name, attempts):
    try:
        # თუ მოთამაშეს არ აქვს ვიზუალი (მაგ. მე-4 მოთამაშე), არ ვხატავთ
        if player_name not in player_turtles:
            return

        t = player_turtles[player_name]
        start_x = player_start_x[player_name]
        
        t.pensize(5)
        
        # კაცუნას ცენტრირება start_x-ის მიხედვით
        if attempts == 5: # თავი
            t.penup()
            t.goto(start_x, 50) # start_x
            t.setheading(0)
            t.pendown()
            t.circle(30) 
            
        elif attempts == 4: # სხეული
            t.penup()
            t.goto(start_x, 50) 
            t.pendown()
            t.goto(start_x, -50)
            
        elif attempts == 3: # მარცხენა ხელი
            t.penup()
            t.goto(start_x, 20)
            t.pendown()
            t.goto(start_x - 40, -20)
            
        elif attempts == 2: # მარჯვენა ხელი
            t.penup()
            t.goto(start_x, 20)
            t.pendown()
            t.goto(start_x + 40, -20)
            
        elif attempts == 1: # მარცხენა ფეხი
            t.penup()
            t.goto(start_x, -50)
            t.pendown()
            t.goto(start_x - 30, -100)
            
        elif attempts == 0: # მარჯვენა ფეხი
            t.penup()
            t.goto(start_x, -50)
            t.pendown()
            t.goto(start_x + 30, -100)
            
            # თვალები (მკვდარი)
            t.penup()
            t.goto(start_x - 10, 70); t.write("X", font=("Arial", 12, "bold"))
            t.goto(start_x + 10, 70); t.write("X", font=("Arial", 12, "bold"))
            
    except Exception: pass

def load_words_from_file():
    words = []
    if os.path.exists(WORDS_FILE):
        try:
            with open(WORDS_FILE, "r", encoding="utf-8") as f:
                words = [line.strip() for line in f.readlines() if line.strip()]
        except Exception:
            pass
    if not words:
        words = ["python", "development", "student", "computer", "keyboard"]
    return words

def save_result(player_name, result):
    try:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        with open(HISTORY_FILE, "a", encoding="utf-8") as file:
            file.write(f"[{timestamp}] მოთამაშე: {player_name} - შედეგი: {result}\n")
    except Exception:
        pass

def delete_history():
    if os.path.exists(HISTORY_FILE):
        try:
            os.remove(HISTORY_FILE)
            print(f"\n[სისტემა] ისტორია წაიშალა.")
        except OSError:
            print(f"[შეცდომა] ვერ წაიშალა.")
    else:
        print("\n[სისტემა] ისტორია ცარიელია.")

def get_display_word(secret_word, guesses):
    display = ""
    for letter in secret_word:
        if letter in guesses:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def validate_input(char):
    if len(char) != 1:
        print("(!) შეიყვანეთ მხოლოდ ერთი სიმბოლო.")
        return False
    if not char.isalpha():
        print("(!) შეიყვანეთ მხოლოდ ასო.")
        return False
    return True

def display_status(attempts_left, guesses, secret_word):
    print("\n" + "="*30)
    print(f"მცდელობები: {attempts_left}")
    print(f"გამოყენებული: {', '.join(sorted(guesses))}")
    print(f"სიტყვა: {get_display_word(secret_word, guesses)}")
    print("="*30)

def play_hangman(players_input, current_scores=None):
    # მოთამაშეების დამუშავება (ერთი ან რამდენიმე)
    if isinstance(players_input, list):
        players = players_input
    else:
        players = [players_input]
    
    player_name = ", ".join(players)

    # ქულების ინიციალიზაცია თუ ცარიელია
    if current_scores is None:
        scores = {p: 0 for p in players}
    else:
        scores = current_scores

    # თამაშის ლოგიკა
    words = load_words_from_file()
    secret_word = random.choice(words).lower()
    guesses = []
    
    # ინდივიდუალური სიცოცხლეების კონფიგურაცია
    max_attempts = 5
    # მოთამაშეთა სიცოცხლეების ლექსიკონის ინიციალიზაცია
    player_lives = {p: max_attempts for p in players}
    
    init_visuals(players)
    
    print(f"\nგამარჯობა, {player_name}! დავიწყოთ.")
    print(f"მიმდინარე ქულები: {scores}")
    
    game_over = False
    won = False
    
    # პირველი ჩვენება (ცარიელი ხაზები)
    current_display = get_display_word(secret_word, guesses)
    update_visual_word(current_display)
    
    current_player_index = 0

    while not game_over:
        # აქტიური მოთამაშეების შემოწმება
        active_players = [p for p in players if player_lives[p] > 0]
        if not active_players:
            game_over = True
            won = False
            break
            
        # დამხმარე სტრიქონი სტატუსისთვის
        status_str = " | ".join([f"{p}: {player_lives[p]}" for p in players])
        display_status(status_str, guesses, secret_word)
        print(f"ქულები: {scores}")
        
        # გადასვლა შემდეგ აქტიურ მოთამაშეზე
        while player_lives[players[current_player_index]] <= 0:
             current_player_index = (current_player_index + 1) % len(players)
             
        current_player = players[current_player_index]

        try:
            guess = input(f"\n{current_player} (Lives: {player_lives[current_player]}), შეიყვანეთ ასო: ").lower().strip()
            
            if not validate_input(guess):
                continue
            
            if guess in guesses:
                print(f"(!) ეს ასო '{guess}' უკვე გამოყენებულია.")
                continue
            
            guesses.append(guess)
            
            if guess in secret_word:
                print(f"(+) სწორია! +10 ქულა {current_player}-ს")
                scores[current_player] += 10
            else:
                player_lives[current_player] -= 1
                draw_hangman_part(current_player, player_lives[current_player])
                print(f"(-) არასწორია. {current_player}-ს დარჩა {player_lives[current_player]} სიცოცხლე.")
                
                if player_lives[current_player] == 0:
                    print(f"\n!!! {current_player} გამოეთიშა თამაშს! !!!")
            
            # გადასვლა შემდეგ მოთამაშეზე (ციკლი გამოტოვებს გავარდნილებს)
            current_player_index = (current_player_index + 1) % len(players)

            # ეკრანის განახლება
            current_display = get_display_word(secret_word, guesses)
            update_visual_word(current_display)
            
            # მოგების პირობა
            if "_" not in get_display_word(secret_word, guesses):
                game_over = True
                won = True
                # ბონუსი მოგებისთვის (ბოლო სწორი ასოს ავტორს ან ყველას ვინც გადარჩა?)
                # მოდი მივცეთ ბონუსი ყველას ვინც ცოცხალია
                for p in players:
                    if player_lives[p] > 0:
                        scores[p] += 50
                print("\n*** ბონუსი +50 ქულა გადარჩენილებს! ***")
                
        except KeyboardInterrupt:
            return scores
        except Exception as e:
            print(f"[!] შეცდომა: {e}")
            continue

    # საბოლოო სტატუსი
    status_str = " | ".join([f"{p}: {player_lives[p]}" for p in players])
    display_status(status_str, guesses, secret_word)
    print(f"საბოლოო ქულები ამ რაუნდში: {scores}")
    
    msg = "YOU WON!" if won else "GAME OVER"
    print(f"\n{'გილოცავთ' if won else 'წააგეთ'}. სიტყვა: {secret_word.upper()}")
    print(f"*** {msg} ***")
    
    # Text removed as per request
    
    save_result(player_name, f"{'მოგება' if won else 'წაგება'} (ქულები: {scores})")
    time.sleep(2)
    return scores

def main_menu():
    while True:
        # მთავარი მენიუ - სესიის დასაწყისი
        try:
            # ანიმაციის გააქტიურება დასაწყისში
            turtle.title("Hangman Game - Console Active")
            # ფანჯრის მომზადება და გადატვირთვა
            turtle.setup(600, 600)
            turtle.clearscreen()
            turtle.hideturtle()
            turtle.penup()
            turtle.goto(0, 0)
            turtle.color("black")
            turtle.write("Welcome!\nPlease check the console to play.", align="center", font=("Arial", 18, "bold"))
        except Exception as e:
            print(f"Window Error: {e}")

        print("\n--- NEW VERSION LOADED ---")
        print("კონსოლური თამაშების ცენტრი v2.0 (ქულებით)")
        
        # 1. მოთამაშეების რეგისტრაცია (სესიის დასაწყისი)
        players = []
        try:
            print("\n[ახალი თამაში]")
            num_players = int(input("შეიყვანეთ მოთამაშეების რაოდენობა: "))
            if num_players < 1:
                num_players = 1
        except ValueError:
            num_players = 1
        
        for i in range(num_players):
            p_name = input(f"მოთამაშე {i+1}-ის სახელი: ").strip()
            if not p_name:
                p_name = f"Player{i+1}"
            players.append(p_name)
        
        # ქულების ინიციალიზაცია
        current_scores = {p: 0 for p in players}
        
        # სესიის ციკლი
        session_active = True
        while session_active:
            print(f"\n--- რაუნდის დასაწყისი ---")
            print(f"მიმდინარე ქულები: {current_scores}")
            
            # თამაშის დაწყება
            current_scores = play_hangman(players, current_scores)
            
            # რაუნდის შემდეგი მენიუ
            print("\n[რაუნდი დასრულდა]")
            print("1. გაგრძელება (ქულების შენარჩუნება)")
            print("2. ახალი თამაში (ქულების განულება / ახალი მოთამაშეები)")
            print("3. გასვლა")
            
            choice = input("აირჩიეთ მოქმედება (1-3): ").strip()
            
            if choice == '1':
                continue # ვაგრძელებთ იგივე ქულებით და მოთამაშეებით
            elif choice == '2':
                session_active = False # სესიის ციკლიდან გამოსვლა -> დაბრუნება მთავარ while True-ში
            elif choice == '3':
                print("ნახვამდის!")
                return # პროგრამიდან გასვლა
            else:
                print("არასწორი არჩევანი, ვიწყებთ ახალ თამაშს (მთავარ მენიუში დაბრუნება)...")
                session_active = False

if __name__ == "__main__":
    main_menu()
