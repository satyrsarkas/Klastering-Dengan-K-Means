clc; clear; close all;
 
image_folder = 'Images Dataset';
filenames = dir(fullfile(image_folder, '*.gif'));
total_images = numel(filenames);
 
area = zeros(1,total_images);
perimeter = zeros(1,total_images);
 
for n = 1:total_images
    full_name = fullfile(image_folder, filenames(n).name);
    our_images = logical(imread(full_name));
    our_images = bwconvhull(our_images,'objects');
    our_images = bwareaopen(our_images,100);
    stats = regionprops(our_images,'All');
    area(n) = stats.Area;
    perimeter(n) = stats.Perimeter;
    X = [area;perimeter]';
end
 
opts = statset('Display','final');
[idx,C] = kmeans(X,3,'Distance','sqeuclidean',...
    'Replicates',5,'Options',opts);
 
figure;
plot(X(idx==1,1),X(idx==1,2),'r.','MarkerSize',24)
hold on
grid on
plot(X(idx==2,1),X(idx==2,2),'g.','MarkerSize',24)
plot(X(idx==3,1),X(idx==3,2),'b.','MarkerSize',24)
plot(C(:,1),C(:,2),'kx',...
    'MarkerSize',15,'LineWidth',3)
legend('Cluster 1','Cluster 2','Cluster 3','Centroids',...
    'Location','best')
title('Cluster Assignments and Centroids')
xlabel('Area')
ylabel('Perimeter')
hold off