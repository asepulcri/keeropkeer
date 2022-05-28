import numpy as np

class Shape:
    def __init__(self, config: np.ndarray, size, leftmost_top_pixel: tuple[int, int]):
        self.config = config
        self.size = size
        self.leftmost_top_pixel = leftmost_top_pixel

    @staticmethod
    def find_leftmost_top_pixel(input_array: np.ndarray) -> tuple[int, int]:
        for i in range(len(input_array[0])):
            if input_array[0, i] == 1:
                return 0, i
        # return 0, np.where(self.config[0] == 1)[0][0]

    def rotate_clockwise_90(self):
        new_config = np.array(
            [[self.config[j][i] for j in range(len(self.config))] for i in range(len(self.config[0]) - 1, -1, -1)])
        return Shape(new_config, self.size, Shape.find_leftmost_top_pixel(new_config))

    def flip_ud(self):
        new_config = np.flipud(self.config)
        return Shape(new_config, self.size, Shape.find_leftmost_top_pixel(new_config))

    def __repr__(self):
        return f"Shape(config: \n{self.config} \nleftmost top pixel: {str(self.leftmost_top_pixel)}"

shape_1_1 = Shape(np.array([[1]]), 1, (0, 0))

shapes_of_1: list[Shape] = [shape_1_1]

shape_2_1 = Shape(np.array([[1, 1]]), 2, (0, 0))
shape_2_2 = shape_2_1.rotate_clockwise_90()

shapes_of_2: list[Shape] = [
    shape_2_1,
    shape_2_2
]

shape_3_1 = Shape(np.array([[1, 1, 1]]), 3, (0, 0))
shape_3_2 = shape_3_1.rotate_clockwise_90()
shape_3_3 = Shape(np.array([[1, 0], [1, 1]]), 3, (0, 0))
shape_3_4 = shape_3_3.rotate_clockwise_90()
shape_3_5 = shape_3_4.rotate_clockwise_90()
shape_3_6 = shape_3_5.rotate_clockwise_90()

shapes_of_3: list[Shape] = [
    shape_3_1,
    shape_3_2,
    shape_3_3,
    shape_3_4,
    shape_3_5,
    shape_3_6,
]

shape_4_1 = Shape(np.array([[1, 1, 1, 1]]), 4, (0, 0))
shape_4_2 = shape_4_1.rotate_clockwise_90()
shape_4_3 = Shape(np.array([[1, 1], [1, 1]]), 4, (0, 0))
shape_4_4 = Shape(np.array([[1, 1, 1], [0, 1, 0]]), 4, (0, 0))
shape_4_5 = shape_4_4.rotate_clockwise_90()
shape_4_6 = shape_4_5.rotate_clockwise_90()
shape_4_7 = shape_4_6.rotate_clockwise_90()
shape_4_8 = Shape(np.array([[1, 1, 1], [1, 0, 0]]), 4, (0, 0))
shape_4_9 = shape_4_8.rotate_clockwise_90()
shape_4_10 = shape_4_9.rotate_clockwise_90()
shape_4_11 = shape_4_10.rotate_clockwise_90()
shape_4_12 = shape_4_8.flip_ud()
shape_4_13 = shape_4_12.rotate_clockwise_90()
shape_4_14 = shape_4_13.rotate_clockwise_90()
shape_4_15 = shape_4_14.rotate_clockwise_90()

shapes_of_4: list[Shape] = [
    shape_4_1,
    shape_4_2,
    shape_4_3,
    shape_4_4,
    shape_4_5,
    shape_4_6,
    shape_4_7,
    shape_4_8,
    shape_4_9,
    shape_4_10,
    shape_4_11,
    shape_4_12,
    shape_4_13,
    shape_4_14,
    shape_4_15,
]

shape_5_1 = Shape(np.array([[1, 1, 1, 1, 1]]), 5, (0, 0))
shape_5_2 = shape_5_1.rotate_clockwise_90()
shape_5_3 = Shape(np.array([[1, 1, 1, 1], [1, 0, 0, 0]]), 5, (0, 0))
shape_5_4 = shape_5_3.rotate_clockwise_90()
shape_5_5 = shape_5_4.rotate_clockwise_90()
shape_5_6 = shape_5_5.rotate_clockwise_90()
shape_5_7 = shape_5_3.flip_ud()
shape_5_8 = shape_5_7.rotate_clockwise_90()
shape_5_9 = shape_5_8.rotate_clockwise_90()
shape_5_10 = shape_5_9.rotate_clockwise_90()
shape_5_11 = Shape(np.array([[1, 1, 1, 1], [0, 0, 1, 0]]), 5, (0, 0))
shape_5_12 = shape_5_11.rotate_clockwise_90()
shape_5_13 = shape_5_12.rotate_clockwise_90()
shape_5_14 = shape_5_13.rotate_clockwise_90()
shape_5_15 = shape_5_11.flip_ud()
shape_5_16 = shape_5_15.rotate_clockwise_90()
shape_5_17 = shape_5_16.rotate_clockwise_90()
shape_5_18 = shape_5_17.rotate_clockwise_90()
shape_5_19 = Shape(np.array([[1, 1, 1], [1, 1, 0]]), 5, (0, 0))
shape_5_20 = shape_5_19.rotate_clockwise_90()
shape_5_21 = shape_5_20.rotate_clockwise_90()
shape_5_22 = shape_5_21.rotate_clockwise_90()
shape_5_23 = shape_5_19.flip_ud()
shape_5_24 = shape_5_23.rotate_clockwise_90()
shape_5_25 = shape_5_24.rotate_clockwise_90()
shape_5_26 = shape_5_25.rotate_clockwise_90()
shape_5_27 = Shape(np.array([[1, 1, 1], [1, 0, 1]]), 5, (0, 0))
shape_5_28 = shape_5_27.rotate_clockwise_90()
shape_5_29 = shape_5_28.rotate_clockwise_90()
shape_5_30 = shape_5_29.rotate_clockwise_90()
shape_5_31 = Shape(np.array([[1, 1, 1], [1, 0, 0], [1, 0, 0]]), 5, (0, 0))
shape_5_32 = shape_5_31.rotate_clockwise_90()
shape_5_33 = shape_5_32.rotate_clockwise_90()
shape_5_34 = shape_5_33.rotate_clockwise_90()
shape_5_35 = Shape(np.array([[1, 0, 0], [1, 1, 1], [1, 0, 0]]), 5, (0, 0))
shape_5_36 = shape_5_35.rotate_clockwise_90()
shape_5_37 = shape_5_36.rotate_clockwise_90()
shape_5_38 = shape_5_37.rotate_clockwise_90()
shape_5_39 = Shape(np.array([[1, 0, 0], [1, 1, 1], [0, 0, 1]]), 5, (0, 0))
shape_5_40 = shape_5_39.rotate_clockwise_90()
shape_5_41 = shape_5_40.flip_ud()
shape_5_42 = shape_5_41.rotate_clockwise_90()
shape_5_43 = Shape(np.array([[1, 0, 0], [1, 1, 1], [0, 1, 0]]), 5, (0, 0))
shape_5_44 = shape_5_43.rotate_clockwise_90()
shape_5_45 = shape_5_44.rotate_clockwise_90()
shape_5_46 = shape_5_45.rotate_clockwise_90()
shape_5_47 = shape_5_46.flip_ud()
shape_5_48 = shape_5_47.rotate_clockwise_90()
shape_5_49 = shape_5_48.rotate_clockwise_90()
shape_5_50 = shape_5_49.rotate_clockwise_90()
shape_5_51 = Shape(np.array([[1, 1, 0, 0], [0, 1, 1, 1]]), 5, (0, 0))
shape_5_52 = shape_5_51.rotate_clockwise_90()
shape_5_53 = shape_5_52.rotate_clockwise_90()
shape_5_54 = shape_5_53.rotate_clockwise_90()
shape_5_55 = shape_5_54.flip_ud()
shape_5_56 = shape_5_55.rotate_clockwise_90()
shape_5_57 = shape_5_56.rotate_clockwise_90()
shape_5_58 = shape_5_57.rotate_clockwise_90()
shape_5_59 = Shape(np.array([[1, 1, 0], [0, 1, 1], [0, 0, 1]]), 5, (0, 0))
shape_5_60 = shape_5_59.rotate_clockwise_90()
shape_5_61 = shape_5_60.rotate_clockwise_90()
shape_5_62 = shape_5_61.rotate_clockwise_90()
shape_5_63 = Shape(np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]), 5, (0, 1))

shapes_of_5: list[Shape] = [
    shape_5_1,
    shape_5_2,
    shape_5_3,
    shape_5_4,
    shape_5_5,
    shape_5_6,
    shape_5_7,
    shape_5_8,
    shape_5_9,
    shape_5_10,
    shape_5_11,
    shape_5_12,
    shape_5_13,
    shape_5_14,
    shape_5_15,
    shape_5_16,
    shape_5_17,
    shape_5_18,
    shape_5_19,
    shape_5_20,
    shape_5_21,
    shape_5_22,
    shape_5_23,
    shape_5_24,
    shape_5_25,
    shape_5_26,
    shape_5_27,
    shape_5_28,
    shape_5_29,
    shape_5_30,
    shape_5_31,
    shape_5_32,
    shape_5_33,
    shape_5_34,
    shape_5_35,
    shape_5_36,
    shape_5_37,
    shape_5_38,
    shape_5_39,
    shape_5_40,
    shape_5_41,
    shape_5_42,
    shape_5_43,
    shape_5_44,
    shape_5_45,
    shape_5_46,
    shape_5_47,
    shape_5_48,
    shape_5_49,
    shape_5_50,
    shape_5_51,
    shape_5_52,
    shape_5_53,
    shape_5_54,
    shape_5_55,
    shape_5_56,
    shape_5_57,
    shape_5_58,
    shape_5_59,
    shape_5_60,
    shape_5_61,
    shape_5_62,
    shape_5_63,
]

shape_6_1 = Shape(np.array([[1, 1, 1, 1, 1, 1]]), 6, (0, 0))
shape_6_2 = shape_6_1.rotate_clockwise_90()
shape_6_3 = Shape(np.array([[1, 1, 1, 1, 1], [0, 0, 0, 0, 1]]), 6, (0, 0))
shape_6_4 = shape_6_3.rotate_clockwise_90()
shape_6_5 = shape_6_4.rotate_clockwise_90()
shape_6_6 = shape_6_5.rotate_clockwise_90()
shape_6_7 = shape_6_6.flip_ud()
shape_6_8 = shape_6_7.rotate_clockwise_90()
shape_6_9 = shape_6_8.rotate_clockwise_90()
shape_6_10 = shape_6_9.rotate_clockwise_90()
shape_6_11 = Shape(np.array([[1, 1, 1, 1, 1], [0, 0, 0, 1, 0]]), 6, (0, 0))
shape_6_12 = shape_6_11.rotate_clockwise_90()
shape_6_13 = shape_6_12.rotate_clockwise_90()
shape_6_14 = shape_6_13.rotate_clockwise_90()
shape_6_15 = shape_6_14.flip_ud()
shape_6_16 = shape_6_15.rotate_clockwise_90()
shape_6_17 = shape_6_16.rotate_clockwise_90()
shape_6_18 = shape_6_17.rotate_clockwise_90()
shape_6_19 = Shape(np.array([[1, 1, 1, 1, 1], [0, 0, 1, 0, 0]]), 6, (0, 0))
shape_6_20 = shape_6_19.rotate_clockwise_90()
shape_6_21 = shape_6_20.rotate_clockwise_90()
shape_6_22 = shape_6_21.rotate_clockwise_90()
shape_6_23 = Shape(np.array([[1, 1, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1]]), 6, (0, 0))
shape_6_24 = shape_6_23.rotate_clockwise_90()
shape_6_25 = shape_6_24.rotate_clockwise_90()
shape_6_26 = shape_6_25.rotate_clockwise_90()
shape_6_27 = shape_6_26.flip_ud()
shape_6_28 = shape_6_27.rotate_clockwise_90()
shape_6_29 = shape_6_28.rotate_clockwise_90()
shape_6_30 = shape_6_29.rotate_clockwise_90()
shape_6_31 = Shape(np.array([[1, 1, 0, 0, 0], [0, 1, 1, 1, 1]]), 6, (0, 0))
shape_6_32 = shape_6_31.rotate_clockwise_90()
shape_6_33 = shape_6_32.rotate_clockwise_90()
shape_6_34 = shape_6_33.rotate_clockwise_90()
shape_6_35 = shape_6_34.flip_ud()
shape_6_36 = shape_6_35.rotate_clockwise_90()
shape_6_37 = shape_6_36.rotate_clockwise_90()
shape_6_38 = shape_6_37.rotate_clockwise_90()
shape_6_39 = Shape(np.array([[1, 1, 1, 1], [1, 0, 0, 1]]), 6, (0, 0))
shape_6_40 = shape_6_39.rotate_clockwise_90()
shape_6_41 = shape_6_40.rotate_clockwise_90()
shape_6_42 = shape_6_41.rotate_clockwise_90()
shape_6_43 = Shape(np.array([[1, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 1]]), 6, (0, 0))
shape_6_44 = shape_6_43.rotate_clockwise_90()
shape_6_45 = shape_6_44.rotate_clockwise_90()
shape_6_46 = shape_6_45.rotate_clockwise_90()
shape_6_47 = Shape(np.array([[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0]]), 6, (0, 0))
shape_6_48 = shape_6_43.rotate_clockwise_90()
shape_6_49 = shape_6_44.rotate_clockwise_90()
shape_6_50 = shape_6_45.rotate_clockwise_90()
shape_6_51 = Shape(np.array([[1, 1, 1, 1], [1, 0, 1, 0]]), 6, (0, 0))
shape_6_52 = shape_6_51.rotate_clockwise_90()
shape_6_53 = shape_6_52.rotate_clockwise_90()
shape_6_54 = shape_6_53.rotate_clockwise_90()
shape_6_55 = shape_6_54.flip_ud()
shape_6_56 = shape_6_55.rotate_clockwise_90()
shape_6_57 = shape_6_56.rotate_clockwise_90()
shape_6_58 = shape_6_57.rotate_clockwise_90()
shape_6_59 = Shape(np.array([[1, 1, 1, 1], [1, 1, 0, 0]]), 6, (0, 0))
shape_6_60 = shape_6_59.rotate_clockwise_90()
shape_6_61 = shape_6_60.rotate_clockwise_90()
shape_6_62 = shape_6_61.rotate_clockwise_90()
shape_6_63 = shape_6_62.flip_ud()
shape_6_64 = shape_6_63.rotate_clockwise_90()
shape_6_65 = shape_6_64.rotate_clockwise_90()
shape_6_66 = shape_6_65.rotate_clockwise_90()
shape_6_67 = Shape(np.array([[1, 0, 0, 0], [1, 1, 1, 1], [0, 1, 0, 0]]), 6, (0, 0))
shape_6_68 = shape_6_67.rotate_clockwise_90()
shape_6_69 = shape_6_68.rotate_clockwise_90()
shape_6_70 = shape_6_69.rotate_clockwise_90()
shape_6_71 = shape_6_70.flip_ud()
shape_6_72 = shape_6_71.rotate_clockwise_90()
shape_6_73 = shape_6_72.rotate_clockwise_90()
shape_6_74 = shape_6_73.rotate_clockwise_90()
shape_6_75 = Shape(np.array([[1, 1, 1, 1], [0, 1, 0, 0], [0, 1, 0, 0]]), 6, (0, 0))
shape_6_76 = shape_6_75.rotate_clockwise_90()
shape_6_77 = shape_6_76.rotate_clockwise_90()
shape_6_78 = shape_6_77.rotate_clockwise_90()
shape_6_79 = shape_6_78.flip_ud()
shape_6_80 = shape_6_79.rotate_clockwise_90()
shape_6_81 = shape_6_80.rotate_clockwise_90()
shape_6_82 = shape_6_81.rotate_clockwise_90()
shape_6_83 = Shape(np.array([[1, 1, 1, 1], [0, 1, 1, 0]]), 6, (0, 0))
shape_6_84 = shape_6_83.rotate_clockwise_90()
shape_6_85 = shape_6_84.rotate_clockwise_90()
shape_6_86 = shape_6_85.rotate_clockwise_90()
shape_6_87 = Shape(np.array([[0, 1, 0, 0], [1, 1, 1, 1], [0, 0, 1, 0]]), 6, (0, 1))
shape_6_88 = shape_6_87.rotate_clockwise_90()
shape_6_89 = shape_6_88.flip_ud()
shape_6_90 = shape_6_89.rotate_clockwise_90()
shape_6_91 = Shape(np.array([[1, 1, 0], [1, 1, 0], [0, 1, 1]]), 6, (0, 0))
shape_6_92 = shape_6_91.rotate_clockwise_90()
shape_6_93 = shape_6_92.rotate_clockwise_90()
shape_6_94 = shape_6_93.rotate_clockwise_90()
shape_6_95 = shape_6_94.flip_ud()
shape_6_96 = shape_6_95.rotate_clockwise_90()
shape_6_97 = shape_6_96.rotate_clockwise_90()
shape_6_98 = shape_6_97.rotate_clockwise_90()
shape_6_99 = Shape(np.array([[1, 1, 0], [1, 1, 1], [0, 1, 0]]), 6, (0, 0))
shape_6_100 = shape_6_99.rotate_clockwise_90()
shape_6_101 = shape_6_100.rotate_clockwise_90()
shape_6_102 = shape_6_101.rotate_clockwise_90()
shape_6_103 = Shape(np.array([[1, 1, 1], [0, 1, 1], [0, 1, 0]]), 6, (0, 0))
shape_6_104 = shape_6_91.rotate_clockwise_90()
shape_6_105 = shape_6_92.rotate_clockwise_90()
shape_6_106 = shape_6_93.rotate_clockwise_90()
shape_6_107 = shape_6_94.flip_ud()
shape_6_108 = shape_6_95.rotate_clockwise_90()
shape_6_109 = shape_6_96.rotate_clockwise_90()
shape_6_110 = shape_6_97.rotate_clockwise_90()
shape_6_111 = Shape(np.array([[1, 1, 1, 0], [0, 1, 1, 1]]), 6, (0, 0))
shape_6_112 = shape_6_111.rotate_clockwise_90()
shape_6_113 = shape_6_112.flip_ud()
shape_6_114 = shape_6_113.rotate_clockwise_90()
shape_6_115 = Shape(np.array([[1, 1, 1], [1, 1, 0], [1, 0, 0]]), 6, (0, 0))
shape_6_116 = shape_6_115.rotate_clockwise_90()
shape_6_117 = shape_6_116.rotate_clockwise_90()
shape_6_118 = shape_6_117.rotate_clockwise_90()
shape_6_119 = Shape(np.array([[1, 1, 1], [1, 1, 1]]), 6, (0, 0))
shape_6_120 = shape_6_119.rotate_clockwise_90()
shape_6_121 = Shape(np.array([[1, 1, 0, 1], [0, 1, 1, 1]]), 6, (0, 0))
shape_6_122 = shape_6_121.rotate_clockwise_90()
shape_6_123 = shape_6_122.rotate_clockwise_90()
shape_6_124 = shape_6_123.rotate_clockwise_90()
shape_6_125 = shape_6_124.flip_ud()
shape_6_126 = shape_6_125.rotate_clockwise_90()
shape_6_127 = shape_6_126.rotate_clockwise_90()
shape_6_128 = shape_6_127.rotate_clockwise_90()
shape_6_129 = Shape(np.array([[1, 1, 1], [1, 0, 1], [1, 0, 0]]), 6, (0, 0))
shape_6_130 = shape_6_129.rotate_clockwise_90()
shape_6_131 = shape_6_130.rotate_clockwise_90()
shape_6_132 = shape_6_131.rotate_clockwise_90()
shape_6_133 = shape_6_132.flip_ud()
shape_6_134 = shape_6_133.rotate_clockwise_90()
shape_6_135 = shape_6_134.rotate_clockwise_90()
shape_6_136 = shape_6_135.rotate_clockwise_90()
shape_6_137 = Shape(np.array([[1, 1, 1], [0, 1, 0], [0, 1, 1]]), 6, (0, 0))
shape_6_138 = shape_6_137.rotate_clockwise_90()
shape_6_139 = shape_6_138.rotate_clockwise_90()
shape_6_140 = shape_6_139.rotate_clockwise_90()
shape_6_141 = shape_6_140.flip_ud()
shape_6_142 = shape_6_141.rotate_clockwise_90()
shape_6_143 = shape_6_142.rotate_clockwise_90()
shape_6_144 = shape_6_143.rotate_clockwise_90()
shape_6_145 = Shape(np.array([[1, 0, 1], [1, 1, 1], [0, 1, 0]]), 6, (0, 0))
shape_6_146 = shape_6_145.rotate_clockwise_90()
shape_6_147 = shape_6_146.rotate_clockwise_90()
shape_6_148 = shape_6_147.rotate_clockwise_90()
shape_6_149 = Shape(np.array([[1, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 1]]), 6, (0, 0))
shape_6_150 = shape_6_149.rotate_clockwise_90()
shape_6_151 = shape_6_150.rotate_clockwise_90()
shape_6_152 = shape_6_151.rotate_clockwise_90()
shape_6_153 = shape_6_152.flip_ud()
shape_6_154 = shape_6_153.rotate_clockwise_90()
shape_6_155 = shape_6_154.rotate_clockwise_90()
shape_6_156 = shape_6_155.rotate_clockwise_90()
shape_6_157 = Shape(np.array([[1, 1, 1, 0], [0, 0, 1, 1], [0, 0, 1, 0]]), 6, (0, 0))
shape_6_158 = shape_6_157.rotate_clockwise_90()
shape_6_159 = shape_6_158.rotate_clockwise_90()
shape_6_160 = shape_6_159.rotate_clockwise_90()
shape_6_161 = shape_6_160.flip_ud()
shape_6_162 = shape_6_161.rotate_clockwise_90()
shape_6_163 = shape_6_162.rotate_clockwise_90()
shape_6_164 = shape_6_163.rotate_clockwise_90()
shape_6_165 = Shape(np.array([[1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 1]]), 6, (0, 0))
shape_6_166 = shape_6_165.rotate_clockwise_90()
shape_6_167 = shape_6_166.rotate_clockwise_90()
shape_6_168 = shape_6_167.rotate_clockwise_90()
shape_6_169 = shape_6_168.flip_ud()
shape_6_170 = shape_6_169.rotate_clockwise_90()
shape_6_171 = shape_6_170.rotate_clockwise_90()
shape_6_172 = shape_6_171.rotate_clockwise_90()
shape_6_173 = Shape(np.array([[1, 0, 0, 0], [1, 1, 1, 1], [0, 0, 1, 0]]), 6, (0, 0))
shape_6_174 = shape_6_173.rotate_clockwise_90()
shape_6_175 = shape_6_174.rotate_clockwise_90()
shape_6_176 = shape_6_175.rotate_clockwise_90()
shape_6_177 = shape_6_176.flip_ud()
shape_6_178 = shape_6_177.rotate_clockwise_90()
shape_6_179 = shape_6_178.rotate_clockwise_90()
shape_6_180 = shape_6_179.rotate_clockwise_90()
shape_6_181 = Shape(np.array([[1, 1, 0, 0], [0, 1, 1, 1], [0, 0, 0, 1]]), 6, (0, 0))
shape_6_182 = shape_6_181.rotate_clockwise_90()
shape_6_183 = shape_6_182.rotate_clockwise_90()
shape_6_184 = shape_6_183.rotate_clockwise_90()
shape_6_185 = shape_6_184.flip_ud()
shape_6_186 = shape_6_185.rotate_clockwise_90()
shape_6_187 = shape_6_186.rotate_clockwise_90()
shape_6_188 = shape_6_187.rotate_clockwise_90()
shape_6_189 = Shape(np.array([[1, 1, 0, 0], [0, 1, 1, 1], [0, 1, 0, 0]]), 6, (0, 0))
shape_6_190 = shape_6_189.rotate_clockwise_90()
shape_6_191 = shape_6_190.rotate_clockwise_90()
shape_6_192 = shape_6_191.rotate_clockwise_90()
shape_6_193 = shape_6_192.flip_ud()
shape_6_194 = shape_6_193.rotate_clockwise_90()
shape_6_195 = shape_6_194.rotate_clockwise_90()
shape_6_196 = shape_6_195.rotate_clockwise_90()
shape_6_197 = Shape(np.array([[1, 1, 0, 0], [0, 1, 1, 1], [0, 0, 1, 0]]), 6, (0, 0))
shape_6_198 = shape_6_197.rotate_clockwise_90()
shape_6_199 = shape_6_198.rotate_clockwise_90()
shape_6_200 = shape_6_199.rotate_clockwise_90()
shape_6_201 = shape_6_200.flip_ud()
shape_6_202 = shape_6_201.rotate_clockwise_90()
shape_6_203 = shape_6_202.rotate_clockwise_90()
shape_6_204 = shape_6_203.rotate_clockwise_90()
shape_6_205 = Shape(np.array([[0, 0, 1, 0], [1, 1, 1, 1], [0, 0, 1, 0]]), 6, (0, 2))
shape_6_206 = shape_6_205.rotate_clockwise_90()
shape_6_207 = shape_6_206.rotate_clockwise_90()
shape_6_208 = shape_6_207.rotate_clockwise_90()
shape_6_209 = Shape(np.array([[1, 1, 1, 0, 0], [0, 0, 1, 1, 1]]), 6, (0, 0))
shape_6_210 = shape_6_209.rotate_clockwise_90()
shape_6_211 = shape_6_210.flip_ud()
shape_6_212 = shape_6_211.rotate_clockwise_90()
shape_6_213 = Shape(np.array([[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1]]), 6, (0, 0))
shape_6_214 = shape_6_213.rotate_clockwise_90()
shape_6_215 = shape_6_214.rotate_clockwise_90()
shape_6_216 = shape_6_215.rotate_clockwise_90()

shapes_of_6: list[Shape] = [
    shape_6_1,
    shape_6_2,
    shape_6_3,
    shape_6_4,
    shape_6_5,
    shape_6_6,
    shape_6_7,
    shape_6_8,
    shape_6_9,
    shape_6_10,
    shape_6_11,
    shape_6_12,
    shape_6_13,
    shape_6_14,
    shape_6_15,
    shape_6_16,
    shape_6_17,
    shape_6_18,
    shape_6_19,
    shape_6_20,
    shape_6_21,
    shape_6_22,
    shape_6_23,
    shape_6_24,
    shape_6_25,
    shape_6_26,
    shape_6_27,
    shape_6_28,
    shape_6_29,
    shape_6_30,
    shape_6_31,
    shape_6_32,
    shape_6_33,
    shape_6_34,
    shape_6_35,
    shape_6_36,
    shape_6_37,
    shape_6_38,
    shape_6_39,
    shape_6_40,
    shape_6_41,
    shape_6_42,
    shape_6_43,
    shape_6_44,
    shape_6_45,
    shape_6_46,
    shape_6_47,
    shape_6_48,
    shape_6_49,
    shape_6_50,
    shape_6_51,
    shape_6_52,
    shape_6_53,
    shape_6_54,
    shape_6_55,
    shape_6_56,
    shape_6_57,
    shape_6_58,
    shape_6_59,
    shape_6_60,
    shape_6_61,
    shape_6_62,
    shape_6_63,
    shape_6_64,
    shape_6_65,
    shape_6_66,
    shape_6_67,
    shape_6_68,
    shape_6_69,
    shape_6_70,
    shape_6_71,
    shape_6_72,
    shape_6_73,
    shape_6_74,
    shape_6_75,
    shape_6_76,
    shape_6_77,
    shape_6_78,
    shape_6_79,
    shape_6_80,
    shape_6_81,
    shape_6_82,
    shape_6_83,
    shape_6_84,
    shape_6_85,
    shape_6_86,
    shape_6_87,
    shape_6_88,
    shape_6_89,
    shape_6_90,
    shape_6_91,
    shape_6_92,
    shape_6_93,
    shape_6_94,
    shape_6_95,
    shape_6_96,
    shape_6_97,
    shape_6_98,
    shape_6_99,
    shape_6_100,
    shape_6_101,
    shape_6_102,
    shape_6_103,
    shape_6_104,
    shape_6_105,
    shape_6_106,
    shape_6_107,
    shape_6_108,
    shape_6_109,
    shape_6_110,
    shape_6_111,
    shape_6_112,
    shape_6_113,
    shape_6_114,
    shape_6_115,
    shape_6_116,
    shape_6_117,
    shape_6_118,
    shape_6_119,
    shape_6_120,
    shape_6_121,
    shape_6_122,
    shape_6_123,
    shape_6_124,
    shape_6_125,
    shape_6_126,
    shape_6_127,
    shape_6_128,
    shape_6_129,
    shape_6_130,
    shape_6_131,
    shape_6_132,
    shape_6_133,
    shape_6_134,
    shape_6_135,
    shape_6_136,
    shape_6_137,
    shape_6_138,
    shape_6_139,
    shape_6_140,
    shape_6_141,
    shape_6_142,
    shape_6_143,
    shape_6_144,
    shape_6_145,
    shape_6_146,
    shape_6_147,
    shape_6_148,
    shape_6_149,
    shape_6_150,
    shape_6_151,
    shape_6_152,
    shape_6_153,
    shape_6_154,
    shape_6_155,
    shape_6_156,
    shape_6_157,
    shape_6_158,
    shape_6_159,
    shape_6_160,
    shape_6_161,
    shape_6_162,
    shape_6_163,
    shape_6_164,
    shape_6_165,
    shape_6_166,
    shape_6_167,
    shape_6_168,
    shape_6_169,
    shape_6_170,
    shape_6_171,
    shape_6_172,
    shape_6_173,
    shape_6_174,
    shape_6_175,
    shape_6_176,
    shape_6_177,
    shape_6_178,
    shape_6_179,
    shape_6_180,
    shape_6_181,
    shape_6_182,
    shape_6_183,
    shape_6_184,
    shape_6_185,
    shape_6_186,
    shape_6_187,
    shape_6_188,
    shape_6_189,
    shape_6_190,
    shape_6_191,
    shape_6_192,
    shape_6_193,
    shape_6_194,
    shape_6_195,
    shape_6_196,
    shape_6_197,
    shape_6_198,
    shape_6_199,
    shape_6_200,
    shape_6_201,
    shape_6_202,
    shape_6_203,
    shape_6_204,
    shape_6_205,
    shape_6_206,
    shape_6_207,
    shape_6_208,
    shape_6_209,
    shape_6_210,
    shape_6_211,
    shape_6_212,
    shape_6_213,
    shape_6_214,
    shape_6_215,
    shape_6_216,
]

all_shapes = {1: shapes_of_1, 2: shapes_of_2, 3: shapes_of_3, 4: shapes_of_4, 5: shapes_of_5, 6: shapes_of_6}
