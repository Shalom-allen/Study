import yfinance as yf
import matplotlib.pyplot as plt

#주식데이터 가져오기 
def get_stock_data(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data

#주식데이터 시각화
def visualize_stock_data(stock_data):
    plt.figure(figsize=(10, 6))
    stock_data['Close'].plot()
    plt.title('Stock Price Over Time')
    plt.xlabel('Data')
    plt.ylabel('Price ($)')
    plt.grid(True)
    plt.show()
    
#메인 함수 
def main():
    #주식 정보 설정
    symbol = 'AAPL'
    start_date = '2024-01-01'
    end_date = '2024-06-01'
    
    #주식데이터 가져오기
    stock_data = get_stock_data(symbol, start_date, end_date)
    
    #주식데이터 시각화
    visualize_stock_data(stock_data)
    
if __name__ == "__main__":
    main()
    