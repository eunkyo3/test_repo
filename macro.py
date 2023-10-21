import webbrowser
import pyautogui
import pyperclip
import time
import random

def open_youtube_and_send_message(message):
    # YouTube 웹사이트 열기
    url = "https://www.youtube.com/"
    webbrowser.open_new(url)
    
    # 웹사이트가 로딩될 때까지 대기 (대기 시간을 필요에 따라 조정할 수 있습니다)
    time.sleep(3)
    
    # 채팅 상자 위치를 색상을 기준으로 찾기 (필요에 따라 수정)
    chat_box_location = pyautogui.locateCenterOnScreen('chat_box.png', confidence=0.9)
    
    if chat_box_location is not None:
        # 채팅 상자 클릭
        pyautogui.click(chat_box_location)
        
        # 메시지를 문자 단위로 입력
        pyperclip.copy(message)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
    else:
        print("채팅 상자를 찾을 수 없습니다. 수동으로 찾아주세요.")

if __name__ == "__main__":
    # 사용자 입력 받기
    messages = [
        "안녕하세요!",
        "반갑습니다.",
        "오늘은 좋은 날이네요!",
        "무엇을 하고 계신가요?",
        "행복한 하루 되세요!"
    ]
    
    while True:
        random_message = random.choice(messages)
        open_youtube_and_send_message(random_message)
        
        # 다음 메시지를 보내기 전 무작위 시간 대기 (필요에 따라 조정)
        time.sleep(random.randint(60, 180))
