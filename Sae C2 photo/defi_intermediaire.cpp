#include <iostream>
#include <opencv2/opencv.hpp>

int main() {
    // Charger l'image d'origine
    cv::Mat image_originale = cv::imread("image.png");

    if (!image_originale.data) {
        std::cerr << "Impossible de charger l'image d'origine." << std::endl;
        return -1;
    }

    // Convertir l'image en niveaux de gris
    cv::Mat image_gris;
    cv::cvtColor(image_originale, image_gris, cv::COLOR_BGR2GRAY);

    // Appliquer l'opérateur de Sobel pour détecter le gradient
    cv::Mat gradient_x, gradient_y;
    cv::Sobel(image_gris, gradient_x, CV_64F, 1, 0, 3);
    cv::Sobel(image_gris, gradient_y, CV_64F, 0, 1, 3);

    // Calculer la magnitude du gradient
    cv::Mat gradient_magnitude;
    cv::magnitude(gradient_x, gradient_y, gradient_magnitude);

    // Afficher l'image d'origine
    cv::imshow("Image d'Origine", image_originale);
    cv::waitKey(0);

    // Afficher la magnitude du gradient
    cv::imshow("Gradient dans l'Image d'Origine", gradient_magnitude);
    cv::waitKey(0);

    return 0;
}
