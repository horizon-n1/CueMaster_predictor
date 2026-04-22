CueMaster AI: Optimal Billiard Move Predictor
CueMaster AI is a computer vision and physics-based tool designed to help players identify the most optimal moves on a pool table after the break. By analyzing a top-down video feed, the system detects ball positions and simulates potential outcomes to recommend the path with the highest probability of success, disregarding advanced techniques like English or curve shots to focus on pure geometric precision.

Core Functionality
Ball Detection & Classification: Uses computer vision to identify the cue ball and all object balls (solids and stripes) from a top-down camera angle.

Table Mapping: Calibrates the table boundaries and pocket locations to create a 2D coordinate system for physics calculations.

Path Simulation: Predicts the trajectory of the cue ball and object balls based on a center-ball hit.

Optimal Move Logic: Evaluates multiple shot possibilities and ranks them based on "ease of win"—considering pocket proximity, shot angle, and post-shot cue ball positioning.

Technical Stack
Computer Vision: [e.g., OpenCV, YOLOv8] for real-time ball detection and coordinate extraction.

Physics Engine: Custom 2D collision physics to simulate ball-to-ball and ball-to-rail interactions.

Language: Python

Data Source: Pre-recorded top-down footage and curated professional match videos.

Camera Calibration & Setup
To ensure maximum accuracy, CueMaster AI is optimized for a top-down (birds-eye) view.

Ideal Setup: A camera mounted directly above the center of the table.

Why Top-Down? Angled views introduce perspective distortion, which requires complex transformation matrices to map back to a true 2D plane. A top-down view allows for direct pixel-to-coordinate mapping.

How It Works
Input: A video frame or image is captured after the break.

Detection: The system identifies the (x, y) coordinates of every ball on the table.

Filtering: The break is ignored to focus on the established game state.

Analysis: The algorithm calculates every possible legal shot.

Recommendation: The "Best Move" is highlighted on-screen, showing the target pocket and the necessary hit angle.

Current Limitations & Roadmap
No Spin/Curve: This version assumes all hits are at the center of the cue ball.

Static Analysis: Currently analyzes the table state after balls have come to a complete rest.

Future Goal: Integrating a recommendation engine that plans 2-3 moves ahead (run-out positioning).

Acknowledgments
Inspired by the work of Bryan.D in real-time pool ball detection. [https://www.youtube.com/watch?v=fw2AP1bXJOo]