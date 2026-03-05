import streamlit as st
import numpy as np
import random

# Reset the game
def reset_game():
    st.session_state.game = np.zeros((3, 3), dtype=int)  # Empty board
    st.session_state.victory = 0
    st.session_state.turn_message = "Your Turn"
    st.session_state.current_player = 1

# Check for a winner
def check_win(board):
    # Check rows
    for i in range(3):
        if all(board[i][j] == 1 for j in range(3)):
            return 1
        if all(board[i][j] == 2 for j in range(3)):
            return 2

    # Check columns
    for j in range(3):
        if all(board[i][j] == 1 for i in range(3)):
            return 1
        if all(board[i][j] == 2 for i in range(3)):
            return 2

    # Check diagonals
    if all(board[i][i] == 1 for i in range(3)):
        return 1
    if all(board[i][i] == 2 for i in range(3)):
        return 2
    if all(board[i][2 - i] == 1 for i in range(3)):
        return 1
    if all(board[i][2 - i] == 2 for i in range(3)):
        return 2

    # Check for tie
    if all(board[i][j] != 0 for i in range(3) for j in range(3)):
        return -1

    return 0

# AI move (random available move)
def ai_move(board):
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]
    if available_moves:
        move = random.choice(available_moves)
        board[move[0]][move[1]] = 2  # AI is O
    return board

# Initialize session state
def initialize():
    if 'game' not in st.session_state:
        st.session_state.player1 = 'Player 1'
        st.session_state.player2 = 'AI'
        st.session_state.game = np.zeros((3, 3), dtype=int)
        st.session_state.victory = 0
        st.session_state.current_player = 1
        st.session_state.turn_message = "Your Turn"

initialize()

st.title("Tic Tac Toe (You vs AI)")
st.button('Reset game', on_click=reset_game)

# Check current victory status
st.session_state.victory = check_win(st.session_state.game)

# Display turn message
if st.session_state.victory == 0:
    st.subheader(st.session_state.turn_message)

# Draw the board
if st.session_state.victory == 0:
    for i in range(3):
        cols = st.columns(3)
        for j in range(3):
            button_label = st.session_state.game[i][j]
            if button_label == 0:
                button_label = "-"
            elif button_label == 1:
                button_label = "X"
            elif button_label == 2:
                button_label = "O"

            with cols[j]:
                if st.button(button_label, key=f'button_{i}_{j}',
                             disabled=st.session_state.game[i][j] != 0 or st.session_state.victory != 0):
                    if st.session_state.victory == 0 and st.session_state.game[i][j] == 0:
                        st.session_state.game[i][j] = 1  # Human move
                        st.session_state.victory = check_win(st.session_state.game)

                        if st.session_state.victory == 0:  # If still ongoing, AI plays
                            st.session_state.turn_message = "AI's Turn"
                            st.session_state.game = ai_move(st.session_state.game)
                            st.session_state.victory = check_win(st.session_state.game)

                            if st.session_state.victory == 0:
                                st.session_state.turn_message = "Your Turn"

# Game results
if st.session_state.victory == 1:
    st.snow()
    st.success('🎉 Player 1 wins!')
elif st.session_state.victory == 2:
    st.balloons()
    st.error('🤖 AI wins!')
elif st.session_state.victory == -1:
    st.warning("🤝 It's a tie! Please click reset to play again.")
