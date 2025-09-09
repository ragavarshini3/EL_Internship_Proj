<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Math Solver AI</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    <style>
        .fade-in {
            animation: fadeIn 1s ease-in-out;
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        .loader-wrapper {
            display: none;
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: rgba(255, 255, 255, 0.8);
            z-index: 1000;
            justify-content: center;
            align-items: center;
        }

        .loader {
            border: 8px solid #f3f3f3;
            border-top: 8px solid #007BFF;
            border-radius: 50%;
            width: 60px;
            height: 60px;
            animation: spin 1s linear infinite;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .download-btn {
            display: block;
            width: 250px;
            margin: 16px auto;
            background: #8000ff;
            color: #fff !important;
            border: none;
            border-radius: 8px;
            padding: 14px 0;
            font-size: 1.1em;
            font-weight: 600;
            text-align: center;
            text-decoration: none;
            transition: background 0.2s;
        }

        .download-btn:hover {
            background: #a259ff;
            color: #fff;
        }

        .result-box {
            text-align: center;
        }

        .top-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 20px;
            background: #007BFF;
            color: #fff;
        }

        .logo {
            font-size: 1.5em;
            font-weight: bold;
        }

        .lang-dropdown {
            margin-left: auto;
        }

        .nav-links {
            margin-left: 20px;
        }

        .nav-links a {
            color: #fff;
            text-decoration: none;
            margin: 0 10px;
        }

        .nav-links a:hover {
            text-decoration: underline;
        }

        /* Additional styles for the navigation bar and app name */
        .nav-links {
            text-align: right;
            margin: 0;
            padding: 18px 36px 0 0;
        }

        .nav-links a {
            color: #8000ff;
            text-decoration: none;
            margin: 0 18px;
            font-size: 1.1em;
            font-weight: 600;
            transition: color 0.2s;
        }

        .nav-links a:hover {
            color: #a259ff;
            text-decoration: underline;
        }

        .app-name {
            text-align: center;
            font-size: 2.2em;
            font-weight: bold;
            color: #8000ff;
            margin-top: 30px;
            margin-bottom: 0;
        }

        /* Hide the original Google Translate element */
        #google_translate_element {
            display: none;
        }
    </style>
    <!-- Google Translate Script -->
    <script type="text/javascript">
function googleTranslateElementInit() {
  new google.translate.TranslateElement({
    pageLanguage: 'en',
    includedLanguages: 'en,ta,hi,te',
    layout: google.translate.TranslateElement.InlineLayout.SIMPLE
  }, 'google_translate_element');
}
</script>
<script src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
</head>
<body>
    <!-- Navigation bar -->
    <div class="nav-links">
        <a href="{{ url_for('solve') }}">Home</a>
        <a href="{{ url_for('faq') }}">FAQ</a>
        <a href="{{ url_for('logout') }}">Logout</a>
    </div>
    <!-- App name/title -->
    <div class="app-name">
        Math Solver AI
    </div>
    <!-- Google Translate Widget -->
    <div id="google_translate_element" style="text-align:center; margin-top:10px;"></div>

    <!-- Main Box -->
    <div class="main-box">
        <h1>Solve Any Math Problem Instantly</h1>
        <p>Enter your problem below and get a step-by-step solution.</p>
        <div class="input-area">
            <form method="POST" action="{{ url_for('solve') }}" enctype="multipart/form-data">
                <select id="example_queries" onchange="document.getElementById('expression').value=this.value;">
                    <option value="">-- Example Queries --</option>
                    <option value="2*x + 3*x">2*x + 3*x</option>
                    <option value="solve(x**2 - 4, x)">solve(x**2 - 4, x)</option>
                    <option value="Area of a circle with radius 5">Area of a circle with radius 5</option>
                </select>
                <textarea id="expression" name="expression" placeholder="Enter your math problem...">{{ spoken_expr }}</textarea><br>
                <input type="file" name="image"><br><br>
                <button class="send-button" type="submit">Solve</button>
            </form>
        </div>

        {% if result %}
        <div class="result-box">
            <p><strong>Result:</strong> {{ result }}</p>
            {% if steps %}
                <pre style="white-space: pre-wrap;">{{ steps.split('\n')[0] }}{% if steps.split('\n')|length > 1 %}
    Explanation: {{ steps.split('\n')[1] }}{% endif %}</pre>
            {% endif %}
            <div class="download-buttons">
                <a href="{{ url_for('download_image') }}" class="download-btn">
                    🖼️ Download Solution Image
                </a>
                <a href="{{ url_for('download_pdf') }}" class="download-btn">
                    📄 Download as PDF
                </a>
            </div>
        </div>
        {% endif %}
    </div>

    <!-- Why Use Section -->
    <div class="why-use-section">
        <h2>Why Use Math Solver AI?</h2>
        <p>Our intelligent system solves your math problems accurately with detailed steps.
           Whether you're a student, parent, or teacher, we've got you covered.</p>
    </div>

    <!-- Feature Section -->
    <section class="feature-section">
        <div class="feature-text">
            <h2>Key Features</h2>
            <p>Our intelligent system uses advanced models to guide you step-by-step in solving problems.</p>
        </div>
        <div class="feature-card">
            <img src="https://png.pngtree.com/background/20240919/original/pngtree-math-problem-solving-robot-depicting-the-concept-of-machine-learning-through-picture-image_10573600.jpg" alt="AI Robot">
            <h3>AI-Powered Solutions</h3>
            <p>Get instant answers using advanced machine learning models trained for mathematical reasoning.</p>
        </div>
    </section>

    <!-- Testimonials Section -->
    <section class="testimonials-section">
        <h2>What Students Say</h2>
        <div class="testimonial-grid">
            <div class="testimonial-card">
                <div class="stars">★★★★★</div>
                <p>"This app helped me ace my calculus exam! It's like having a tutor 24/7."</p>
                <div class="name">Varshini R.</div>
                <div class="role">Student, B.Sc. Mathematics</div>
            </div>
            <div class="testimonial-card">
                <div class="stars">★★★★★</div>
                <p>"I use this with my kids for homework—it explains everything clearly."</p>
                <div class="name">Ravi K.</div>
                <div class="role">Parent</div>
            </div>
            <div class="testimonial-card">
                <div class="stars">★★★★☆</div>
                <p>"Super helpful during my online classes. Easy to use and fast."</p>
                <div class="name">Sneha M.</div>
                <div class="role">Engineering Student</div>
            </div>
        </div>
    </section>

    <!-- How It Works Section -->
    <section class="how-it-works">
        <div class="steps">
            <h2>How It Works</h2>
            <p><span class="step-number">1</span> Enter your question in the box above.</p>
            <p><span class="step-number">2</span> Click the "Solve" button to process your query.</p>
            <p><span class="step-number">3</span> View the result and download the solution.</p>
        </div>
        <div class="supported-topics">
            <h2>Supported Topics</h2>
            <h4>Algebra</h4>
            <ul>
                <li>Equations</li>
                <li>Expressions</li>
                <li>Quadratic</li>
            </ul>
            <h4>Calculus</h4>
            <ul>
                <li>Differentiation</li>
                <li>Integration</li>
            </ul>
            <h4>Statistics</h4>
            <ul>
                <li>Mean, Median</li>
                <li>Standard Deviation</li>
            </ul>
        </div>
    </section>

    <!-- JavaScript -->
    <script>
        function showLoader() {
            document.getElementById('loader').style.display = 'flex';
        }

        function hideLoader() {
            document.getElementById('loader').style.display = 'none';
        }

        document.querySelector('form')?.addEventListener('submit', function () {
            showLoader();
        });
    </script>
</body>
</html>
