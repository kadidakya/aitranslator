from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>منصة التداول المصغرة - الشموع والأسعار الحية</title>
        <!-- استدعاء مكتبة الرسوم البيانية الخفيفة من TradingView -->
        <script src="https://unpkg.com/lightweight-charts/dist/lightweight-charts.standalone.production.js"></script>
        <style>
            body {
                font-family: Tahoma, sans-serif;
                background: #0d1117;
                color: #c9d1d9;
                margin: 0;
                padding: 15px;
                text-align: center;
            }
            h2 { color: #58a6ff; margin-bottom: 20px; }
            .container {
                display: flex;
                flex-direction: column;
                gap: 20px;
                max-width: 600px;
                margin: 0 auto;
            }
            .card {
                background: #161b22;
                border: 1px solid #30363d;
                border-radius: 12px;
                padding: 15px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.4);
                text-align: left;
            }
            .header-card {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 10px;
                direction: ltr;
            }
            .coin-title {
                font-size: 18px;
                font-weight: bold;
                color: #f0f6fc;
            }
            .price-tag {
                font-size: 16px;
                color: #00ffcc;
                font-family: monospace;
            }
            /* مكان الرسم البياني */
            .chart-container {
                width: 100%;
                height: 200px;
            }
            .footer {
                margin-top: 25px;
                font-size: 12px;
                color: #8b949e;
            }
        </style>
    </head>
    <body>

        <h2>📈 منصة الرسوم البيانية والشموع الحية</h2>
        <div class="container" id="coins-wrapper">
            <!-- سيتم تعبئة العملات والرسوم البيانية تلقائياً عبر الجافاسكريبت من بينانس -->
        </div>

        <div class="footer">
            <p>يعمل عبر Termux - بيانات حية مباشرة من سوق Binance</p>
        </div>

        <script>
            // قائمة العملات المراد عرضها
            const symbols = [
                { symbol: 'BTCUSDT', name: 'Bitcoin (BTC/USDT)' },
                { symbol: 'ETHUSDT', name: 'Ethereum (ETH/USDT)' },
                { symbol: 'SOLUSDT', name: 'Solana (SOL/USDT)' }
            ];

            const wrapper = document.getElementById('coins-wrapper');

            async function initCharts() {
                for (let item of symbols) {
                    // إنشاء بطاقة لكل عملة
                    const card = document.createElement('div');
                    card.className = 'card';
                    card.innerHTML = `
                        <div class="header-card">
                            <span class="coin-title">${item.name}</span>
                            <span class="price-tag" id="price-${item.symbol}">جاري التحميل...</span>
                        </div>
                        <div class="chart-container" id="chart-${item.symbol}"></div>
                    `;
                    wrapper.appendChild(card);

                    // إنشاء الرسم البياني للشموع (Candlestick Chart)
                    const chartDom = document.getElementById(`chart-${item.symbol}`);
                    const chart = LightweightCharts.createChart(chartDom, {
                        layout: {
                            background: { type: 'solid', color: '#161b22' },
                            textColor: '#c9d1d9',
                        },
                        grid: {
                            vertLines: { color: '#30363d' },
                            horzLines: { color: '#30363d' },
                        },
                        timeScale: {
                            timeVisible: true,
                            secondsVisible: true,
                        },
                    });

                    const candlestickSeries = chart.addCandlestickSeries({
                        upColor: '#3fb950',      // شمعة صعود خضراء
                        downColor: '#f85149',    // شمعة هبوط حمراء
                        borderVisible: false,
                        wickUpColor: '#3fb950',
                        wickDownColor: '#f85149',
                    });

                    // جلب بيانات الشموع التاريخية (Klines) من بينانس لفترة 1 دقيقة
                    try {
                        const res = await fetch(`https://api.binance.com/api/v3/klines?symbol=${item.symbol}&interval=1m&limit=50`);
                        const data = await res.json();
                        
                        const candleData = data.map(d => ({
                            time: d[0] / 1000, // التحويل إلى ثوانٍ
                            open: parseFloat(d[1]),
                            high: parseFloat(d[2]),
                            low: parseFloat(d[3]),
                            close: parseFloat(d[4])
                        }));

                        candlestickSeries.setData(candleData);
                        chart.timeScale().fitContent();

                        // تحديث السعر الفوري أعلى الشارت
                        const lastCandle = candleData[candleData.length - 1];
                        document.getElementById(`price-${item.symbol}`).innerText = lastCandle.close + " $";

                    } catch (e) {
                        console.log("خطأ في جلب بيانات الشموع لـ " + item.symbol);
                    }
                }
            }

            initCharts();
        </script>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

