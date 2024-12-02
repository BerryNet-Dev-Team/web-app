-- Connect to DB --
\c docker

-- INSERT FIRST USER AND ITS REQUESTS --
INSERT INTO public.users("name", "lastName", "email", "password")
VALUES ('Liora', 'Melith', 'test@testing.com', 'Pass$612345');

INSERT INTO public.requests("userId", "description", "originalScansUrls", "generatedImagesUrls", "createdOn", "completedOn")
VALUES (
  1,
  'Segmentar tejido cerebral en resonancias magnéticas',
  '{"https://cdn.pixabay.com/photo/2020/09/26/23/56/brain-5605289_640.png", "https://cdn.pixabay.com/photo/2014/11/01/18/21/brain-512758_640.png"}',
  '{"https://cdn.pixabay.com/photo/2017/04/16/21/13/brain-2235831_640.png", "https://cdn.pixabay.com/photo/2022/05/04/14/44/brain-7174144_640.png"}',
  '2024-10-12 15:25:45',
  '2024-10-12 15:30:45'
);

INSERT INTO public.requests("userId", "description", "originalScansUrls", "generatedImagesUrls", "createdOn", "completedOn")
VALUES (
  1,
  'Etiquetado semántico de estructuras cerebrales en MRI',
  '{"https://cdn.pixabay.com/photo/2020/09/26/23/56/brain-5605289_640.png", "https://cdn.pixabay.com/photo/2014/11/01/18/21/brain-512758_640.png"}',
  '{"https://cdn.pixabay.com/photo/2017/04/16/21/13/brain-2235831_640.png", "https://cdn.pixabay.com/photo/2022/05/04/14/44/brain-7174144_640.png"}',
  '2024-10-12 15:25:45',
  '2024-10-12 15:30:45'
);

INSERT INTO public.requests("userId", "description", "originalScansUrls", "generatedImagesUrls", "createdOn", "completedOn")
VALUES (
  1,
  'Detección de lesiones en materia blanca en MRI',
  '{"https://cdn.pixabay.com/photo/2020/09/26/23/56/brain-5605289_640.png", "https://cdn.pixabay.com/photo/2014/11/01/18/21/brain-512758_640.png"}',
  '{"https://cdn.pixabay.com/photo/2017/04/16/21/13/brain-2235831_640.png", "https://cdn.pixabay.com/photo/2022/05/04/14/44/brain-7174144_640.png"}',
  '2024-10-12 15:25:45',
  '2024-10-12 15:30:45'
);


-- INSERT SECOND USER AND ITS REQUESTS --
INSERT INTO public.users("name", "lastName", "email", "password")
VALUES ('Jorvik', 'Elandar', 'test2@testing.com', 'Pass$612345');

INSERT INTO public.requests("userId", "description", "originalScansUrls", "generatedImagesUrls", "createdOn", "completedOn")
VALUES (
  2,
  'Segmentación automática de los ventrículos cerebrales',
  '{"https://cdn.pixabay.com/photo/2020/09/26/23/56/brain-5605289_640.png", "https://cdn.pixabay.com/photo/2014/11/01/18/21/brain-512758_640.png"}',
  '{"https://cdn.pixabay.com/photo/2017/04/16/21/13/brain-2235831_640.png", "https://cdn.pixabay.com/photo/2022/05/04/14/44/brain-7174144_640.png"}',
  '2024-10-12 15:25:45',
  '2024-10-12 15:30:45'
);

INSERT INTO public.requests("userId", "description", "originalScansUrls", "generatedImagesUrls", "createdOn", "completedOn")
VALUES (
  2,
  'Identificar regiones de tejido anormal en MRI cerebral',
  '{"https://cdn.pixabay.com/photo/2020/09/26/23/56/brain-5605289_640.png", "https://cdn.pixabay.com/photo/2014/11/01/18/21/brain-512758_640.png"}',
  '{"https://cdn.pixabay.com/photo/2017/04/16/21/13/brain-2235831_640.png", "https://cdn.pixabay.com/photo/2022/05/04/14/44/brain-7174144_640.png"}',
  '2024-10-12 15:25:45',
  '2024-10-12 15:30:45'
);

INSERT INTO public.requests("userId", "description", "originalScansUrls", "generatedImagesUrls", "createdOn", "completedOn")
VALUES (
  2,
  'Detección de lesiones en materia blanca en MRI',
  '{"https://cdn.pixabay.com/photo/2020/09/26/23/56/brain-5605289_640.png", "https://cdn.pixabay.com/photo/2014/11/01/18/21/brain-512758_640.png"}',
  '{"https://cdn.pixabay.com/photo/2017/04/16/21/13/brain-2235831_640.png", "https://cdn.pixabay.com/photo/2022/05/04/14/44/brain-7174144_640.png"}',
  '2024-10-12 15:25:45',
  '2024-10-12 15:30:45'
);

-- INSERT THIRD USER AND ITS REQUESTS --
INSERT INTO public.users("name", "lastName", "email", "password")
VALUES ('Saphira', 'Vexel', 'test3@testing.com', 'Pass$612345');

INSERT INTO public.requests("userId", "description", "originalScansUrls", "generatedImagesUrls", "createdOn", "completedOn")
VALUES (
  3,
  'Segmentar materia gris y blanca en MRI cerebral',
  '{"https://cdn.pixabay.com/photo/2020/09/26/23/56/brain-5605289_640.png", "https://cdn.pixabay.com/photo/2014/11/01/18/21/brain-512758_640.png"}',
  '{"https://cdn.pixabay.com/photo/2017/04/16/21/13/brain-2235831_640.png", "https://cdn.pixabay.com/photo/2022/05/04/14/44/brain-7174144_640.png"}',
  '2024-10-12 15:25:45',
  '2024-10-12 15:30:45'
);

INSERT INTO public.requests("userId", "description", "originalScansUrls", "generatedImagesUrls", "createdOn", "completedOn")
VALUES (
  3,
  'Segmentación de regiones del hipocampo en MRI',
  '{"https://cdn.pixabay.com/photo/2020/09/26/23/56/brain-5605289_640.png", "https://cdn.pixabay.com/photo/2014/11/01/18/21/brain-512758_640.png"}',
  '{"https://cdn.pixabay.com/photo/2017/04/16/21/13/brain-2235831_640.png", "https://cdn.pixabay.com/photo/2022/05/04/14/44/brain-7174144_640.png"}',
  '2024-10-12 15:25:45',
  '2024-10-12 15:30:45'
);

INSERT INTO public.requests("userId", "description", "originalScansUrls", "generatedImagesUrls", "createdOn", "completedOn")
VALUES (
  3,
  'Detectar anomalías cerebrales en imágenes de MRI',
  '{"https://cdn.pixabay.com/photo/2020/09/26/23/56/brain-5605289_640.png", "https://cdn.pixabay.com/photo/2014/11/01/18/21/brain-512758_640.png"}',
  '{"https://cdn.pixabay.com/photo/2017/04/16/21/13/brain-2235831_640.png", "https://cdn.pixabay.com/photo/2022/05/04/14/44/brain-7174144_640.png"}',
  '2024-10-12 15:25:45',
  '2024-10-12 15:30:45'
);