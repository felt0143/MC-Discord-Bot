import datetime
import os
import yfinance as yf
import matplotlib.pyplot as plt


def ticker_exists(symbol):
    ticker = yf.Ticker(symbol)
    return ticker.info['regularMarketPrice'] is not None


def get_ticker_history(symbol, period='1d', interval='1m'):
    ticker = yf.Ticker(symbol)
    return ticker.history(period, interval)


def create_price_history_plot_png(symbol, period='1d', interval='1m'):
    # Check if symbol exists first
    if not ticker_exists(symbol):
        return ''

    ticker_history = get_ticker_history(symbol, period, interval)

    figure = plt.figure()
    figure.set_figwidth(8)
    figure.set_figheight(5)
    plt.title(f'{symbol} {period} @ {interval}')
    plt.ylabel('USD ($)')
    plt.plot(ticker_history.index, ticker_history['Close'])
    filename = f'.\\data\\{symbol}_{period}_{interval}_{datetime.date.today()}.png'
    figure.autofmt_xdate()
    plt.savefig(filename)

    return filename


def delete_price_history_plot_png(filename):
    if os.path.exists(filename):
        os.remove(filename)
