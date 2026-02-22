from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            body {
                background: linear-gradient(-45deg, #ff6b6b, #ee5a6f, #c44569, #5a67d8, #667eea, #764ba2);
                background-size: 400% 400%;
                animation: gradientShift 20s ease infinite;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                overflow: hidden;
                position: relative;
            }
            
            @keyframes gradientShift {
                0% { background-position: 0% 50%; }
                25% { background-position: 100% 50%; }
                50% { background-position: 100% 100%; }
                75% { background-position: 0% 0%; }
                100% { background-position: 0% 50%; }
            }
            
            /* Floating particles background */
            .particles {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                pointer-events: none;
                z-index: 0;
            }
            
            .particle {
                position: absolute;
                background: rgba(255, 255, 255, 0.5);
                border-radius: 50%;
                pointer-events: none;
            }
            
            .particle1 {
                width: 80px;
                height: 80px;
                top: 10%;
                left: 10%;
                animation: float 20s infinite ease-in-out;
                background: rgba(255, 107, 107, 0.3);
            }
            
            .particle2 {
                width: 60px;
                height: 60px;
                top: 70%;
                right: 10%;
                animation: float 25s infinite ease-in-out reverse;
                background: rgba(90, 103, 216, 0.3);
            }
            
            .particle3 {
                width: 40px;
                height: 40px;
                top: 50%;
                left: 5%;
                animation: float 30s infinite ease-in-out;
                background: rgba(118, 75, 162, 0.3);
            }
            
            @keyframes float {
                0%, 100% { transform: translateY(0px) translateX(0px); }
                25% { transform: translateY(-50px) translateX(30px); }
                50% { transform: translateY(-100px) translateX(-30px); }
                75% { transform: translateY(-50px) translateX(30px); }
            }
            
            .container {
                text-align: center;
                background: rgba(255, 255, 255, 0.98);
                padding: 80px 60px;
                border-radius: 30px;
                box-shadow: 0 30px 80px rgba(0, 0, 0, 0.3);
                backdrop-filter: blur(20px);
                max-width: 700px;
                animation: slideInContainer 0.9s cubic-bezier(0.34, 1.56, 0.64, 1);
                border: 2px solid rgba(255, 255, 255, 0.8);
                position: relative;
                z-index: 10;
            }
            
            .container::before {
                content: '';
                position: absolute;
                top: -50%;
                left: -50%;
                width: 200%;
                height: 200%;
                background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.1), transparent);
                animation: shine 3s infinite;
                pointer-events: none;
            }
            
            @keyframes shine {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
            
            @keyframes slideInContainer {
                from {
                    opacity: 0;
                    transform: translateY(-50px) scale(0.95);
                }
                to {
                    opacity: 1;
                    transform: translateY(0) scale(1);
                }
            }
            
            h1 {
                background: linear-gradient(135deg, #ff6b6b, #c44569, #5a67d8, #667eea);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                font-size: 64px;
                margin: 0 0 25px 0;
                font-weight: 800;
                animation: fadeInScale 1s ease-out;
                letter-spacing: -1px;
            }
            
            @keyframes fadeInScale {
                from {
                    opacity: 0;
                    transform: scale(0.7) rotateX(45deg);
                }
                to {
                    opacity: 1;
                    transform: scale(1) rotateX(0deg);
                }
            }
            
            p {
                color: #333;
                font-size: 32px;
                margin: 20px 0;
                font-weight: 600;
                animation: fadeInUp 1.2s ease-out;
                background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }
            
            @keyframes fadeInUp {
                from {
                    opacity: 0;
                    transform: translateY(30px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            
            .emoji-section {
                font-size: 80px;
                margin: 40px 0;
                animation: bounce 2.5s ease-in-out infinite;
                animation-delay: 0s;
            }
            
            @keyframes bounce {
                0%, 100% { transform: translateY(0) scale(1); }
                50% { transform: translateY(-20px) scale(1.1); }
            }
            
            .separator-line {
                width: 60px;
                height: 4px;
                background: linear-gradient(90deg, #ff6b6b, #667eea);
                margin: 30px auto;
                border-radius: 2px;
                animation: expandWidth 1.5s ease-out;
            }
            
            @keyframes expandWidth {
                from { width: 0; }
                to { width: 60px; }
            }
            
            .button-container {
                margin-top: 40px;
                display: none;
            }
            
            .stats {
                display: none;
            }
            
            /* Additional Advanced Styles */
            .glow-effect {
                position: absolute;
                width: 300px;
                height: 300px;
                background: radial-gradient(circle, rgba(102, 126, 234, 0.15) 0%, transparent 70%);
                border-radius: 50%;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                animation: pulseGlow 3s ease-in-out infinite;
                pointer-events: none;
            }
            
            @keyframes pulseGlow {
                0%, 100% { transform: translate(-50%, -50%) scale(1); opacity: 0.5; }
                50% { transform: translate(-50%, -50%) scale(1.2); opacity: 1; }
            }
            
            .gradient-text-effect {
                background: linear-gradient(90deg, #ff6b6b, #c44569, #5a67d8, #667eea, #764ba2, #f093fb, #ff6b6b);
                background-size: 200% auto;
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                animation: gradientFlow 8s linear infinite;
            }
            
            @keyframes gradientFlow {
                0% { background-position: 0% center; }
                100% { background-position: 200% center; }
            }
            
            /* Card hover effect */
            .container:hover {
                transform: translateY(-10px);
                box-shadow: 0 40px 100px rgba(0, 0, 0, 0.2);
                background: rgba(255, 255, 255, 1);
            }
            
            /* Neon glow text effect */
            .neon-glow {
                text-shadow: 0 0 10px rgba(102, 126, 234, 0.8),
                            0 0 20px rgba(102, 126, 234, 0.6),
                            0 0 30px rgba(102, 126, 234, 0.4);
                animation: neonFlicker 3s infinite;
            }
            
            @keyframes neonFlicker {
                0%, 100% { text-shadow: 0 0 10px rgba(102, 126, 234, 0.8), 0 0 20px rgba(102, 126, 234, 0.6); }
                50% { text-shadow: 0 0 20px rgba(102, 126, 234, 1), 0 0 40px rgba(102, 126, 234, 0.8); }
            }
            
            /* Smooth transitions */
            * {
                transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
            }
        </style>
    </head>
    <body>
        <div class="particles">
            <div class="particle particle1"></div>
            <div class="particle particle2"></div>
            <div class="particle particle3"></div>
        </div>
        
        <div class="container">
            <h1>Hello Rajesh 👋</h1>
            <div class="separator-line"></div>
            <p>Have a Nice Day! 😊</p>
            <div class="emoji-section">😄✨🚀</div>
            <div class="glow-effect"></div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)