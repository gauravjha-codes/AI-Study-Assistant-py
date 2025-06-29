<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Study Assistant README</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            background-color: #f9f9f9;
            color: #333;
        }
        h1, h2, h3 {
            color: #24292e;
            border-bottom: 1px solid #eaecef;
            padding-bottom: 0.3em;
        }
        h1 {
            font-size: 2em;
        }
        h2 {
            font-size: 1.5em;
        }
        h3 {
            font-size: 1.25em;
        }
        p {
            margin: 0.5em 0;
        }
        ul {
            margin: 0.5em 0;
            padding-left: 20px;
        }
        code {
            background-color: #f6f8fa;
            padding: 2px 4px;
            border-radius: 3px;
            font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
            font-size: 85%;
        }
        pre {
            background-color: #f6f8fa;
            padding: 16px;
            border-radius: 6px;
            overflow-x: auto;
        }
        pre code {
            background-color: transparent;
            padding: 0;
        }
        a {
            color: #0366d6;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .section {
            margin-bottom: 20px;
        }
        .license {
            font-size: 0.9em;
            color: #586069;
        }
    </style>
</head>
<body>
    <h1>AI Study Assistant</h1>

    <div class="section">
        <h2>Overview</h2>
        <p>AI Study Assistant is a Python-based desktop application designed to aid students in their study process. Built with <code>customtkinter</code> for the GUI, it integrates with the Gemini AI API for generating study notes, questions, and summaries, and the Dictionary API for word definitions. The app features three main tabs: <strong>Study Assistant</strong>, <strong>Planner</strong>, and <strong>Dictionary</strong>, providing a comprehensive tool for note-taking, study planning, and vocabulary lookup.</p>
    </div>

    <div class="section">
        <h2>Features</h2>
        <ul>
            <li><strong>Study Assistant Tab</strong>:
                <ul>
                    <li>Generate detailed notes from input text using Gemini AI.</li>
                    <li>Create multiple-choice questions based on generated notes.</li>
                    <li>Summarize notes into concise bullet points.</li>
                    <li>Export notes, questions, and summaries to a PDF file.</li>
                </ul>
            </li>
            <li><strong>Planner Tab</strong>:
                <ul>
                    <li>Generate a day-wise study plan based on input topics and durations.</li>
                    <li>Save and load study plans as JSON files.</li>
                    <li>Track task completion with toggleable "Done/Undone" status buttons.</li>
                </ul>
            </li>
            <li><strong>Dictionary Tab</strong>:
                <ul>
                    <li>Look up word definitions, synonyms, and examples using the Dictionary API.</li>
                    <li>Display results in a clean, readable format.</li>
                </ul>
            </li>
        </ul>
    </div>

    <div class="section">
        <h2>Requirements</h2>
        <ul>
            <li>Python 3.8+</li>
            <li>Libraries:
                <ul>
                    <li><code>customtkinter</code></li>
                    <li><code>google-generativeai</code></li>
                    <li><code>fpdf</code></li>
                    <li><code>Pillow</code></li>
                    <li><code>requests</code></li>
                </ul>
            </li>
            <li>Gemini API key (replace <code>YOUR_GEMINI_API</code> in the code with a valid key)</li>
        </ul>
    </div>

    <div class="section">
        <h2>Installation</h2>
        <ol>
            <li>Clone the repository:
                <pre><code>git clone https://github.com/yourusername/ai-study-assistant.git
cd ai-study-assistant</code></pre>
            </li>
            <li>Install dependencies:
                <pre><code>pip install customtkinter google-generativeai fpdf Pillow requests</code></pre>
            </li>
            <li>Obtain a Gemini API key from <a href="https://makersuite.google.com/">Google AI Studio</a> and update the <code>GEN_API_KEY</code> variable in the code.</li>
            <li>Run the application:
                <pre><code>python ai_study_assistant.py</code></pre>
            </li>
        </ol>
    </div>

    <div class="section">
        <h2>Usage</h2>
        <ul>
            <li><strong>Study Assistant</strong>:
                <ul>
                    <li>Enter text in the input box and click "Generate Notes" to create detailed notes.</li>
                    <li>Use "Generate Questions" to create multiple-choice questions from the notes.</li>
                    <li>Click "Generate Summary" for a concise summary of the notes.</li>
                    <li>Export all content to a PDF using the "Export To PDF" button.</li>
                </ul>
            </li>
            <li><strong>Planner</strong>:
                <ul>
                    <li>Input topics and durations (e.g., "Math: 2 hours, Physics: 3 hours") and click "Generate Plan" to create a study schedule.</li>
                    <li>Toggle task status between "Done" and "Undone".</li>
                    <li>Save or load plans using the "Save Tasks" and "Load Tasks" buttons.</li>
                </ul>
            </li>
            <li><strong>Dictionary</strong>:
                <ul>
                    <li>Enter a word and click "Search" to retrieve definitions, synonyms, and examples.</li>
                </ul>
            </li>
        </ul>
    </div>

    <div class="section">
        <h2>Screenshots</h2>
        <p><em>(Add screenshots of the application here, e.g., Study Assistant tab, Planner tab, Dictionary tab)</em></p>
    </div>

    <div class="section">
        <h2>Contributing</h2>
        <p>Contributions are welcome! Please follow these steps:</p>
        <ol>
            <li>Fork the repository.</li>
            <li>Create a new branch (<code>git checkout -b feature-branch</code>).</li>
            <li>Make your changes and commit (<code>git commit -m "Add new feature"</code>).</li>
            <li>Push to the branch (<code>git push origin feature-branch</code>).</li>
            <li>Open a pull request.</li>
        </ol>
    </div>

    <div class="section">
        <h2>License</h2>
        <p class="license">This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>
    </div>

    <div class="section">
        <h2>Acknowledgments</h2>
        <ul>
            <li><a href="https://github.com/TomSchimansky/CustomTkinter">CustomTkinter</a> for the modern GUI framework.</li>
            <li><a href="https://makersuite.google.com/">Google Generative AI</a> for content generation.</li>
            <li><a href="https://dictionaryapi.dev/">Dictionary API</a> for word information.</li>
            <li>Created by Gaurav.</li>
        </ul>
    </div>
</body>
</html>
